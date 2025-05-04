pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        PYTHON = 'python3'
    }

    stages {
        stage('Clone Repository') {
            steps {
                echo "Cloning repository..."
                // Git is automatically used by Jenkins via SCM section
            }
        }

        stage('Set up virtualenv') {
            steps {
                sh """
                    ${PYTHON} -m venv ${VENV_DIR}
                    source ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                """
            }
        }

        stage('Apply Migrations') {
            steps {
                sh """
                    source ${VENV_DIR}/bin/activate
                    ${PYTHON} manage.py migrate
                """
            }
        }

        stage('Collect Static Files') {
            steps {
                sh """
                    source ${VENV_DIR}/bin/activate
                    ${PYTHON} manage.py collectstatic --noinput
                """
            }
        }

        stage('Run Tests (optional)') {
            steps {
                sh """
                    source ${VENV_DIR}/bin/activate
                    ${PYTHON} manage.py test
                """
            }
        }

        stage('Run Server (Dev)') {
            steps {
                sh """
                    source ${VENV_DIR}/bin/activate
                    nohup ${PYTHON} manage.py runserver 0.0.0.0:8000 &
                """
            }
        }
    }
}
