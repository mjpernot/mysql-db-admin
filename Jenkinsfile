pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
        stage('Test') {
            steps {
                dir ('lib') {
                    git branch: "mod/292", credentialsId: "2cfb403c-be21-4fac-94d7-c8cd5c531feb", url: "https://gitlab.code.dicelab.net/JAC-IDM/python-lib.git"
                }
                dir ('mongo_lib') {
                    git branch: "mod/421", credentialsId: "2cfb403c-be21-4fac-94d7-c8cd5c531feb", url: "https://gitlab.code.dicelab.net/JAC-IDM/mongo-lib.git"
                }
                dir ('mongo_lib/lib') {
                    git branch: "mod/286", credentialsId: "2cfb403c-be21-4fac-94d7-c8cd5c531feb", url: "https://gitlab.code.dicelab.net/JAC-IDM/python-lib.git"
                }
                dir ('mysql_lib') {
                    git branch: "mod/531", credentialsId: "2cfb403c-be21-4fac-94d7-c8cd5c531feb", url: "https://gitlab.code.dicelab.net/JAC-IDM/mysql-lib.git"
                }
                dir ('mysql_lib/lib') {
                    git branch: "mod/286", credentialsId: "2cfb403c-be21-4fac-94d7-c8cd5c531feb", url: "https://gitlab.code.dicelab.net/JAC-IDM/python-lib.git"
                }
                sh """
                virtualenv test_env
                source test_env/bin/activate
                pip2 install mock==2.0.0 --user
                pip2 install mysql-connector-python==8.0.22 --user
                pip2 install pymongo==3.8.0 --user
                pip2 install simplejson==2.0.9 --user
                pip2 install psutil==5.4.3 --user
                /usr/bin/python ./test/unit/mysql_db_admin/_process_json.py
                /usr/bin/python ./test/unit/mysql_db_admin/_process_non_json.py
                /usr/bin/python ./test/unit/mysql_db_admin/help_message.py
                /usr/bin/python ./test/unit/mysql_db_admin/run_analyze.py
                /usr/bin/python ./test/unit/mysql_db_admin/analyze.py
                /usr/bin/python ./test/unit/mysql_db_admin/check.py
                /usr/bin/python ./test/unit/mysql_db_admin/checksum.py
                /usr/bin/python ./test/unit/mysql_db_admin/detect_dbs.py
                /usr/bin/python ./test/unit/mysql_db_admin/listdbs.py
                /usr/bin/python ./test/unit/mysql_db_admin/optimize.py
                /usr/bin/python ./test/unit/mysql_db_admin/process_request.py
                /usr/bin/python ./test/unit/mysql_db_admin/proc_all_dbs.py
                /usr/bin/python ./test/unit/mysql_db_admin/proc_all_tbls.py
                /usr/bin/python ./test/unit/mysql_db_admin/proc_some_tbls.py
                /usr/bin/python ./test/unit/mysql_db_admin/run_check.py
                /usr/bin/python ./test/unit/mysql_db_admin/run_checksum.py
                /usr/bin/python ./test/unit/mysql_db_admin/run_optimize.py
                /usr/bin/python ./test/unit/mysql_db_admin/status.py
                /usr/bin/python ./test/unit/mysql_db_admin/run_program.py
                /usr/bin/python ./test/unit/mysql_db_admin/main.py
                deactivate
                rm -rf test_env
                """
            }
        }
        stage('SonarQube analysis') {
            steps {
                sh './test/unit/sonarqube_code_coverage.sh'
                sh 'rm -rf lib'
                sh 'rm -rf mongo_lib'
                sh 'rm -rf mysql_lib'
                script {
                    scannerHome = tool 'sonar-scanner';
                }
                withSonarQubeEnv('Sonar') {
                    sh "${scannerHome}/bin/sonar-scanner -Dproject.settings=sonar-project.JACIDM.properties"
                }
            
            }
        }
        stage('Artifactory upload') {
            steps {
                script {
                    server = Artifactory.server('Artifactory')
                    server.credentialsId = 'art-svc-highpoint-dev'
                    uploadSpec = """{
                        "files": [
                            {
                                "pattern": "./*.py",
                                "recursive": false,
                                "excludePatterns": [],
                                "target": "pypi-proj-local/highpoint/mysql-db-admin/"
                            },
                            {
                                "pattern": "./*.txt",
                                "recursive": false,
                                "excludePatterns": [],
                                "target": "pypi-proj-local/highpoint/mysql-db-admin/"
                            },
                            {
                                "pattern": "./*.md",
                                "recursive": false,
                                "excludePatterns": [],
                                "target": "pypi-proj-local/highpoint/mysql-db-admin/"
                            },
                            {
                                "pattern": "*.TEMPLATE",
                                "recursive": true,
                                "excludePatterns": [],
                                "target": "pypi-proj-local/highpoint/mysql-db-admin/config/"
                            }
                        ]
                    }"""
                    server.upload(uploadSpec)
                }
            }
        }
    }
    post {
        always {
            cleanWs disableDeferredWipeout: true
        }
    }
}
