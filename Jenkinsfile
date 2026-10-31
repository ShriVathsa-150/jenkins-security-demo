
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'python3 app.py'
            }
        }

        stage('Testing') {
            steps {
                sh 'python3 -m unittest test_app.py'
            }
        }

        stage('SAST Scan') {
            steps {
                sh 'pip install bandit'
                sh 'bandit -r .'
            }
        }

        stage('SCA Scan') {
            steps {
                sh 'pip install safety'
                sh 'safety scan'
            }
        }

        stage('Security Check') {
            steps {
                echo 'Security scanning completed'
            }
        }
    }
}

