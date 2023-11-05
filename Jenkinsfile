pipeline {
    agent {
        docker {
            image 'python:3.9.13-alpine3.16'
        }
    }

    environment {
        DJANGO_SETTINGS_MODULE = 'crm_backend.crm_backend.settings'  
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Navigate to crm_backend') {
            steps {
                dir('crm_backend') {
                    // 进入 crm_backend 目录并执行后端操作
                    sh 'pip install -r requirements.txt'  // 安装依赖
                    //sh 'python manage.py migrate'  // 数据库迁移
                    sh 'python manage.py test crm_app.tests'  // 运行后端测试
                }
            }
        }

    }
}
