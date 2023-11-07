pipeline {
    agent any

    environment {
        DJANGO_SETTINGS_MODULE = 'crm_backend.settings'  
    }

    stages {
        stage('Start PostgreSQL Container') {
            steps {
                script {
                    // 使用 Docker 启动 PostgreSQL 容器，并将其连接到 my-network
                    sh 'docker run --name my-postgres -e POSTGRES_PASSWORD=mysecretpassword -d -p 5432:5432 postgres:latest'
                    
                    // 等待 PostgreSQL 容器启动
                    sh 'until docker exec -i my-postgres psql -U postgres -c "SELECT 1"; do sleep 1; done'
                }
            }
        }

        stage('Navigate to crm_backend') {
            agent {
                docker {
                    image 'python:3.9.13-alpine3.16'
                }
            }
            steps {
                dir('crm_backend') {
                    // 进入 crm_backend 目录并执行后端操作
                    sh 'echo "Installing dependencies..."'
                    sh 'pip install -r requirements.txt'  // 安装依赖
                    sh 'echo "Running backend tests..."'
                    sh 'python manage.py test crm_app.tests'  // 运行后端测试
                }
            }
        }
        stage('Deploy Backend Server') {
             steps {
                 dir('crm_backend') {
                    // 进入 crm_backend 目录并执行部署操作
                    sh 'echo "Deploying backend server..."'

                    // 构建Django应用的Docker镜像
                    sh 'docker build -t my-django-app .'

                    // 运行Django应用的Docker容器
                    sh 'docker run -d -p 8000:8000 --name django-container my-django-app'
                    }
                }
        }

    }
}
