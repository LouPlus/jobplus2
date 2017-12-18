from jobplus.app import create_app

#    app.register_blueprint(job)

# development config

app = create_app('development')

if __name__ == '__main__':
    
    app.run()


