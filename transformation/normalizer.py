import numpy as np
import pandas as pd


class JsonStatDataset:

    def __init__(self, data: dict):
        self.data = data
        self.title = data.get("label")
        self.dimensions = data["id"]
        self.sizes = data["size"]
        self._categories = self._read_categories()
        self._positions, self._values = self._read_values()

    def _read_categories(self):
        result = {}
        for dim in self.dimensions:
            cat = self.data["dimension"][dim]["category"]
            index = cat["index"]
            codes = sorted(index, key=index.get) if isinstance(index, dict) else list(index)
            result[dim] = {"codes": codes, "labels": cat.get("label", {})}
        return result

    def _read_values(self):
        values = self.data.get("value", {})
        if isinstance(values, dict):
            positions = np.fromiter((int(k) for k in values), dtype=np.int64, count=len(values))
            vals = np.array(list(values.values()), dtype="float64")
        else:
            arr = np.array(values, dtype="float64")  # None -> nan
            positions = np.flatnonzero(~np.isnan(arr))
            vals = arr[positions]
        return positions, vals

    @property
    def n_cells(self) -> int:
        """Celle teoriche (prodotto di tutte le dimensioni)."""
        return int(np.prod(self.sizes))

    @property
    def n_values(self) -> int:
        """Celle che contengono davvero un dato."""
        return len(self._values)

    def describe(self, n_examples: int = 5):
        print(f"Titolo: {self.title}")
        print(f"Celle teoriche: {self.n_cells:,} | Celle con dato: {self.n_values:,}")
        for dim, size in zip(self.dimensions, self.sizes):
            info = self._categories[dim]
            esempi = [(c, info["labels"].get(c, c)) for c in info["codes"][:n_examples]]
            print(f"\n- {dim} ({size} valori) -> {self.data['dimension'][dim].get('label')}")
            print(f"  esempi: {esempi}")

    def dimension_values(self, dim: str) -> dict:
        info = self._categories[dim]
        return {c: info["labels"].get(c, c) for c in info["codes"]}

    def to_dataframe(self, use_labels: bool = False) -> pd.DataFrame:
        coords = np.unravel_index(self._positions, self.sizes)

        columns = {}
        for dim, idx in zip(self.dimensions, coords):
            info = self._categories[dim]
            cats = info["codes"]
            if use_labels:
                cats = [info["labels"].get(c, c) for c in cats]
            columns[dim] = pd.Categorical.from_codes(idx, categories=cats)

        df = pd.DataFrame(columns)
        df["value"] = self._values
        return df