CircleCI Orb
======

- CircleCI Orb 官方教程: https://circleci.com/docs/2.0/orb-intro/
- 搜索社区提供的 Orb, 尽量找那些 CircleCI Partner 提供的 Orb: https://circleci.com/docs/2.0/circleci-images/

**Orb 是用来做什么的**

一句话介绍: Orb 解决了 CI/CD 代码不容易被参数化, 复用的问题.

首先你要理解 CircleCI 的一个 CI/CD ``Pipeline`` 中关于 ``executor``, ``job``, ``command``, ``steps``, ``workflow`` 的概念. 如果不懂, 请先阅读 .. 之后 再来看本文档.

Orb 相对于 CircleCI pipeline script, 就相当于 Jenkins Shared Library (JSL) 之于 Jenkins pipeline script, 就相当于 Python Library 之于 Python. 例如, JSL 中定义的函数可以被调用, 用来生成整个 pipeline script, 也可以在 JSL 定义 declaritive 用来生成复杂的 declaritive 片段. 而 Python Library 中的变量, 函数, 类 都可以被复用. 而对于 Orb 本质上还是一个 CircleCI pipeline script 的判断, 其中定义的 executors, commands, jobs 都可以被参数化调用.

Orb 有官方的 registry 平台. 该平台跟 dockerHub 很像, 就相当于 docker image 之于 dockerHub 的关系.

**Orb 是如何工作的**

Orb 在被官方注册过之后, 标识符通常为 ``${OrganzationName}/${OrbName}``. 你可以用这个标识符来 Import Orb. 然后就可以在你的 CircleCI pipeline script 中使用 Orb 定义过的 Job, Command 和 Executor 了. 如果你已经了解 Job, Command 和 Executor 在 pipeline script 中的功能和重要性, 那就很容易理解了.

** CircleCI 中的核心概念**

- Steps: Run commands (such as installing dependencies or running tests) and shell scripts to do the work required for your project.
- Jobs: Responsible for running a series of steps that perform commands.
- Workflows: Responsible for orchestrating multiple jobs.
- Pipeline: Represents the entirety of your configuration. Available in CircleCI Cloud only.
- Executors: 定义了 Runtime 环境
