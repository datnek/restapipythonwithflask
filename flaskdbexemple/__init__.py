from config.settings import  init_app


init_app.change_env("development")

init_app.app.app_context().push()


from controllers import homeController , studentContoller, professorContoller, productContoller, authgradeContoller





if __name__ == '__main__':
    #print("{0}".format(init_app.read_json_param()))
    init_app.app.run()
    #flaskdbexemple.run(debug=True)
