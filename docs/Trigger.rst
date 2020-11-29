Trigger a Build
======

.. contents::
    :depth:
    :local:

如何触发 Build

Reference:

- Triggers: https://circleci.com/docs/2.0/triggers/

每次 Commit, Push 都运行一个 Build
------

在 Project Settings -> Advance 菜单中, 勾选 GitHub Status Updates (此为默认行为)


每次 Pull Request 都运行一个 Build
------

在 Project Settings -> Advance 菜单中, 勾选 Only buld pull requests


每隔一段时间 或者 每天定时定点 Build
------

.. code-block::

    workflows:
    version: 2
    commit:
        jobs:
        - test
        - deploy
    nightly:
        triggers: #use the triggers key to indicate a scheduled build
        - schedule:
            cron: "0 0 * * *" # use cron syntax to set the schedule
            filters:
                branches:
                only:
                    - master
                    - beta
        jobs:
        - coverage

参考资料: https://circleci.com/docs/2.0/triggers/#scheduled-builds


整个 workflow 或是 某一个 job (通常是部署) 需要在 APP 里手动点击同意
------

.. code-block::

    workflows:
    version: 2
    build-test-and-approval-deploy:
        jobs:
        - build
        - test1:
            requires:
                - build
        - test2:
            requires:
                - test1
        - hold:
            type: approval # requires that an in-app button be clicked by an appropriate member of the project to continue.
            requires:
            - test2
        - deploy:
            requires:
                - hold

参考资料: https://circleci.com/docs/2.0/triggers/#manual-approval


手动用 CLI 执行一个 Build
------

curl -u ${CIRCLE_API_USER_TOKEN}: \
     -d 'build_parameters[CIRCLE_JOB]=deploy_docker' \
     https://circleci.com/api/v1.1/project/<vcs-type>/<org>/<repo>/tree/<branch>

参考资料: https://circleci.com/docs/2.0/triggers/#trigger-a-job-using-curl-and-your-api-token
