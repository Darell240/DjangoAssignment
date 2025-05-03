pipeline {
    agent any
    stages {
        stage('Deploy Django') {
            steps {
                sh '''
                    cd /home/ubuntu/projects/DjangoAssignment
                    git pull origin main
                    source venv/bin/activate
                    pip install -r requirements.txt
                    nohup python manage.py runserver 0.0.0.0:8000 &
                '''
            }
        }
    }
}
