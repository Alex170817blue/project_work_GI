from webapp import create_app

if __name__ == "__main__":
    # il reloader riavvia il processo e interrompe i thread in corso
    create_app().run(debug=False, use_reloader=False)