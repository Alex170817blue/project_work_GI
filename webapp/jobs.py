import threading
import uuid

JOBS = {}
_lock = threading.Lock()


def start_job(fn, **kwargs):
    """Avvia fn in background. Restituisce l'id del job, o None se ce n'è già uno in corso."""
    if not _lock.acquire(blocking=False):
        return None

    job_id = uuid.uuid4().hex[:8]
    JOBS[job_id] = {"status": "running", "log": []}

    def log(msg):
        JOBS[job_id]["log"].append(str(msg))

    def target():
        try:
            fn(log=log, **kwargs)
            JOBS[job_id]["status"] = "done"
        except Exception as e:
            log(f"ERRORE: {e}")
            JOBS[job_id]["status"] = "error"
        finally:
            _lock.release()

    threading.Thread(target=target, daemon=True).start()
    return job_id