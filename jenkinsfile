pipeline {
    agent any

    environment {
        ENV_NAME = "${ENV_NAME}" // Uses Jenkins global env variable
    }

    stages {
        stage('Check Branch') {
            when {
                expression { env.BRANCH_NAME == 'main' }
            }
            steps {
                script {
                    echo "Branch Name: ${env.BRANCH_NAME}"
                    echo "Running pipeline for main branch!"
                }
            }
        }
        
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
    }
}
