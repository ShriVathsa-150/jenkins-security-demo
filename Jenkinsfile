
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/ShriVathsa-150/jenkins-security-demo.git'
            }
        }

        stage('Build') {
            steps {
                sh '''
                    python3 --version
                    python3 -m venv venv
                    venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Testing') {
            steps {
                sh '''
                    venv/bin/pytest test_app.py \
                    --junitxml=test-results.xml
                '''
            }
            post {
                always {
                    junit allowEmptyResults: true,
                          testResults: 'test-results.xml'
                }
            }
        }

        stage('SAST - Bandit') {
            steps {
                script {
                    int status = sh(
                        returnStatus: true,
                        script: '''
                            venv/bin/bandit -r app.py \
                            -f json -o bandit-report.json
                        '''
                    )

                    if (status != 0) {
                        echo "Bandit found security issues or encountered an error."
                        currentBuild.result = 'UNSTABLE'
                    }
                }
            }
            post {
                always {
                    archiveArtifacts artifacts: 'bandit-report.json',
                                     allowEmptyArchive: true
                }
            }
        }

        stage('SCA - pip-audit') {
            steps {
                script {
                    int status = sh(
                        returnStatus: true,
                        script: '''
                            venv/bin/pip-audit \
                            -r requirements.txt \
                            --format json \
                            --output dependency-report.json
                        '''
                    )

                    if (status != 0) {
                        echo "Dependency vulnerabilities found or scan error."
                        currentBuild.result = 'UNSTABLE'
                    }
                }
            }
            post {
                always {
                    archiveArtifacts artifacts: 'dependency-report.json',
                                     allowEmptyArchive: true
                }
            }
        }

    }

    post {
        always {
            echo 'Jenkins CI/CD Security Pipeline Completed'
        }

        success {
            echo 'Build and security checks completed successfully.'
        }

        unstable {
            echo 'Security findings detected. Review the reports.'
        }

        failure {
            echo 'Pipeline failed. Check Jenkins console output.'
        }
    }
}
