class CLI:
    def run_dev(self):
        from src.wsgi import app
        app.run(debug=True)

    def run_product_seeder(self):
        from src.wsgi import app
        from src.cli.run_product_seeder import run
        with app.app_context():
            run()

    def run_user_seeder(self):
        from src.wsgi import app
        from src.cli.run_user_seeder import run
        with app.app_context():
            run()
