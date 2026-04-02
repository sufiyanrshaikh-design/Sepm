pipeline {
    agent any
    triggers {
        pollSCM(&#39;* * * * *&#39;)
    }
    environment {
        IMAGE_NAME = "devops-app"
        CONTAINER_NAME = "devops-container"
        APP_PORT = "5000"
    }
    stages {
        stage(&#39;Build Docker Image&#39;) {
            steps {
                bat "docker build --no-cache -t %IMAGE_NAME% ."
            }
        }
        stage(&#39;Stop Existing Containers&#39;) {
            steps {

                bat &#39;&#39;&#39;
                for /f "tokens=*" %%i in (&#39;docker ps -q&#39;) do docker stop %%i
                for /f "tokens=*" %%i in (&#39;docker ps -aq&#39;) do docker rm %%i
                &#39;&#39;&#39;
            }
        }
        stage(&#39;Run New Container&#39;) {
            steps {
                bat "docker run -d --name %CONTAINER_NAME% -p
%APP_PORT%:%APP_PORT% %IMAGE_NAME%"
            }
        }
    }
}