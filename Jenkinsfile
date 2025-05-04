pipeline {
    agent any

    environment {
        PROJECT_DIR = "/var/lib/jenkins/workspace/Django-Deploy"
        VENV_DIR = "${PROJECT_DIR}/venv"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                sh """
                    python3 -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                """
            }
        }

        stage('Run Migrations') {
            steps {
                sh """
                    . ${VENV_DIR}/bin/activate
                    python manage.py migrate
                """
            }
        }

        stage('Collect Static Files') {
            steps {
                sh """
                    . ${VENV_DIR}/bin/activate
                    mkdir -p ${PROJECT_DIR}/staticfiles
                    python manage.py collectstatic --noinput
                """
            }
        }

        stage('Restart Services') {
            steps {
                script {
                    try {
                        sh """
                            sudo systemctl restart gunicorn
                            sudo systemctl restart nginx
                        """
                    } catch (err) {
                        echo "Failed to restart services: ${err}"
                    }
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
