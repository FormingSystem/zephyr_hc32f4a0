---
id: learning.zephyr-docs.project-governance.page-10
title: TSC项目角色
kind: reference
status: maintained
domains: [zephyr, governance, documentation]
source_url: https://docs.zephyrproject.org/latest/project/project_roles.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="tsc-project-roles"></a>

<a id="project-roles"></a>

# 第10章\_TSC 项目角色（TSC Project Roles）

原文：[官方页面](https://docs.zephyrproject.org/latest/project/project_roles.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

<a id="id1"></a>

## 10.1 项目角色（Project Roles）

可以贡献者（Contributor）、协作者（Collaborator）或维护者（Maintainer）的身份参与 Zephyr 项目。

贡献者（Contributor）：向项目贡献代码、文档或其他资源的任何社区成员。

协作者（Collaborator）：积极参与项目一个或多个领域的贡献者。

维护者（Maintainer）：负责项目特定领域或子系统的主要协作者；需要时也在 TSC 中代表该领域。

这里的领域（Area）指 Zephyr 代码库中的特定子系统、组件或模块，例如网络、文件系统、设备驱动、架构支持和板级支持包（开发板及 SoC 定义），但不限于这些。

项目的每个领域应至少有一名维护者，可以有多名协作者。根据规模和复杂度，也可有多名维护者，但应把人数控制在切实可行的最低水平，以确保有效管理和决策。

<a id="contributor"></a>

<a id="id2"></a>

### 10.1.1 贡献者（Contributor）

贡献者是希望在任意层面参与项目贡献的开发者。

贡献者享有以下权利并承担以下职责：

- 有权贡献代码、文档、翻译、美术素材等。

- 有权报告缺陷并提出改进建议。

- 有权参与评审他人的贡献。

- 有权参与功能开发流程。

- 有责任遵守已作出的决定；欢迎提供新的相关信息，以重新讨论决定。

- 对自身贡献引入的问题和缺陷负责。

- 有责任遵守社区规则。

- 参与讨论和贡献评审时，有责任提供建设性建议。

- 有责任遵守项目行为准则（Code of Conduct）：[https://github.com/zephyrproject-rtos/zephyr/blob/main/CODE_OF_CONDUCT.md](https://github.com/zephyrproject-rtos/zephyr/blob/main/CODE_OF_CONDUCT.md)。

<a id="zephyr-contributor-badge"></a>

#### 10.1.1.1 Zephyr 贡献者徽章（Zephyr Contributor Badge）

首次向 Zephyr 项目提交的贡献被合并后，即有资格申领 Zephyr 贡献者徽章。这种数字徽章可展示于网站、博客和社交媒体个人资料等位置，用于展示对 Zephyr 的参与并提高项目知名度。

可以填写 [Zephyr 贡献者徽章申请表](https://forms.gle/oCw9iAPLhUsHTapc8)，申请徽章。

<a id="collaborator"></a>

<a id="id3"></a>

### 10.1.2 协作者（Collaborator）

协作者是同时参与 Zephyr 源码维护的贡献者。按照以贡献和能力为依据的原则，决策时他们的意见具有更高权重。

通过持续参与项目成为协作者，包括在一段时间内作出重要贡献，以及参与至少一个领域的开发和评审。

若申请成为协作者，应提交 PR，将自己加入 MAINTAINERS 文件中某领域的 `collaborators` 部分，并通知该领域维护者。新增人员须经该领域维护者批准。 相关链接：[MAINTAINERS 文件（MAINTAINERS File）](#maintainers-file)。

除贡献者的权利与职责外，协作者还享有和承担：

- 有权与所属领域维护者一起制定该领域的短期和中期目标。

- 有责任参与功能开发流程。

- 有责任在合理时间内评审相关代码变更。

- 有责任使代码质量达到预期水平。

- 有责任参与社区讨论。

- 适当时有责任指导新贡献者。

- 开展质量验证和发布时，有责任参与这些流程。

协作者对 PR 提出的修改请求应由原提交者处理。若请求不符合项目预期或指南，或双方存在分歧，指定负责人（Assignee）有责任推进评审并解决分歧。 相关链接：[评审预期](../contributing/P004_审查者职责.md#reviewer-expectations)。

协作者对 PR 的批准计入合并所需的最少批准数；合并还可能受其他条件约束。

<a id="maintainer"></a>

<a id="id4"></a>

### 10.1.3 维护者（Maintainer）

维护者是同时负责理解、引导和预判某 Zephyr 源码领域需求的协作者。

个人可以通过长期、持续且有实质意义的贡献成为某领域维护者，包括：

- 对该领域作出重要技术贡献。

- 积极参与开发流程，包括代码评审和设计讨论。

- 熟悉该领域的架构、约束和演进。

将新领域或子系统引入项目的原作者，若展现出获得认可的专业能力及长期投入，也可获得维护者身份。

在所有情况下，维护者身份既体现技术责任，也体现持续参与该领域支持社区。

若申请成为维护者，应提交 PR，将自己加入 MAINTAINERS 文件中某领域的 `maintainers` 部分，并通知该领域现有维护者。新增人员须经该领域维护者批准。 相关链接：[MAINTAINERS 文件（MAINTAINERS File）](#maintainers-file)。

通常只有一名维护者；视领域情况，也可能由多名维护者共同承担职责。

除贡献者和协作者的权利与职责外，维护者还享有和承担：

- 有权确定相关子系统或参与领域的总体架构。

- 有权与协作者和提交者共同作出相关子系统或领域的决定，参见 [PR 技术升级处理（PR Technical Escalation）](../contributing/P003_贡献者职责.md#pr-technical-escalation)。

- 有责任向 TSC 传达相关子系统或领域的发展方向。

- 有责任确保项目所有贡献在合理时间内获得评审。

- 有责任执行行为准则。维护者作为社区领导者，应以身作则维护准则，为所有人创造友好、包容的环境。

- 有责任对所属代码领域的静态分析问题进行分诊，参见[静态代码分析（Static Code Analysis）](../contributing/P002_贡献指南.md#static-analysis)。

维护者对 PR 的批准计入合并所需的最少批准数；合并还可能受其他条件约束。

<a id="teams-and-supporting-activities"></a>

## 10.2 团队与支持活动（Teams and Supporting Activities）

<a id="assignee"></a>

### 10.2.1 指定负责人（Assignee）

指定负责人是 PR 所修改领域的一名维护者。

系统依据变更代码自动设置负责人。无法自动设置，或其他负责人更合适时，其他维护者或发布工程团队可以设置负责人；后一种情况须在评论中记录变更理由。

- 有责任推动 PR 达到可合并状态。

- 有权撤销过时、无关或不符合[评审预期](../contributing/P004_审查者职责.md#reviewer-expectations)的评审，并向其他维护者、开发者和贡献者征求评审。

- 在问题或修改请求处理完毕之前，有权阻止 PR 合并。

- 若负责人本人是原始代码提交者，有责任重新指派 PR。

- 征求受影响子系统维护者的批准。

- 有责任推进 PR 技术升级处理流程。 相关链接：[PR 技术升级处理（PR Technical Escalation）](../contributing/P003_贡献者职责.md#pr-technical-escalation)。

<a id="static-analysis-audit-team"></a>

### 10.2.2 静态分析审计团队（Static Analysis Audit Team）

静态分析审计团队与发布工程团队密切协作，确保发布周期内报告的静态分析缺陷得到适当处理。其权利和职责如下：

- 有权撤销静态分析工具（如 Coverity）中不符合项目预期的分诊结果。

- 有责任告知代码负责人不恰当的分类。

- 若相关代码负责人未妥善处理问题，有责任向 TSC 报告。

加入静态分析审计团队（Joining the Static Analysis Audit team）

- 深度参与项目、并具备一定静态分析专长的贡献者。

<a id="release-engineering-team"></a>

<a id="id5"></a>

### 10.2.3 发布工程团队（Release Engineering Team）

由参与多个领域的活跃维护者组成的团队。

- 发布工程团队成员应按既定轮换节奏和选择流程担任发布经理。

- 轮换节奏和选择流程由发布工程团队制定，并经 TSC 批准。

- 团队直接向 TSC 汇报。

发布工程团队享有以下权利并承担以下职责：

- 有权按项目规则将代码变更合入 Zephyr 代码树。

- 有权回退破坏代码库的任何变更。

- 有权关闭连续 `<N>` 个月没有活动的陈旧变更。

> 译注——未定义阈值：`<N>` 是原文占位符，本页没有给出具体月数；不能把它解释为已经确定的自动关闭期限。

- 有责任接受并遵循 TSC 的指示。

- 有责任与维护者协调代码合并。

- 对于已获相应维护者批准且符合合并条件的贡献，无论来源和所属领域如何，均有责任合并。

- 有责任使 Zephyr 代码库保持可工作且通过 CI 的状态。

加入发布工程团队（Joining the Release Engineering team）

- 深度参与项目的维护者可由一名有投票权的 TSC 成员提名加入发布工程团队；经现有 TSC 投票成员批准，候选人可成为团队成员。

- 为保证团队正常运作，TSC 应定期评估发布工程团队采用的流程、适当规模和成员构成，例如确保成员分布于多个地区和时区。

<a id="release-manager"></a>

### 10.2.4 发布经理（Release Manager）

发布经理是负责依照特定版本的项目里程碑与路线图，推动该版本完成的维护者。

- 发布经理必须获得 TSC 批准。

发布经理是发布工程团队成员，除该团队权利与职责外，还享有和承担：

- 有权在代码冻结里程碑之后管理和协调所有代码合并；M3 详见[项目管理概览](https://wiki.zephyrproject.org/Program-Management)。

- 有责任推动和协调本次发布的问题分诊流程。

- 有责任编写本次发布的发布说明。

- 有责任及时向项目全部利益相关方，包括整个社区，通报发布状态。

- 有责任与质量保证（Quality Assurance，QA）和验证人员协调；在重大变更和重要里程碑之前，直接或通过 QA 验证变更。

<a id="roles-permissions"></a>

### 10.2.5 角色与权限（Roles / Permissions）

<a id="id7"></a>

**项目角色与 GitHub 权限（Project Roles vs GitHub Permissions）**

> 译注——角色与权限：表中 x 表示原表标记的权限关系，空格保留原意。权限列 Owner 指 GitHub 所有者角色，和发布里程碑表中的负责人，以及 PR 的 Assignee 不是同一含义；项目协作者与 GitHub 权限名 Collaborator 也不能直接等同。具体账户权限仍以实际组织配置为准，本表不是授权证明。

|  |  | 管理员（Admin） | 合并权限（Merge Rights） | 成员（Member） | 负责人（Owner） | 协作者（Collaborator） |
| --- | --- | --- | --- | --- | --- | --- |
| 主要角色（Main Roles） | 贡献者（Contributor） |  |  |  |  | x |
|  | 协作者（Collaborator） |  |  | x |  |  |
|  | 维护者（Maintainer） |  |  | x |  |  |
| 支持角色（Supportive Roles） | 质量保证／验证（QA/Validation） |  |  | x |  | x |
|  | 开发与运维（DevOps） | x |  |  |  |  |
|  | 系统管理员（System Admin） | x |  |  | x |  |
|  | 发布工程团队（Release Engineering） |  | x | x |  |  |

<a id="role-retirement"></a>

## 10.3 角色退出（Role Retirement）

经 TSC 或其代表批准担任项目角色、但不再积极履行相应权利与职责的人员，可能被 TSC 要求退出该角色。

不活跃维护者或协作者的退出，通过从 Zephyr 仓库 MAINTAINERS 文件相关部分移除其 GitHub 用户名体现，可由 TSC、其代表或本人发起。维护者也可发起移除所属领域的不活跃协作者。 相关链接：[MAINTAINERS 文件（MAINTAINERS File）](#maintainers-file)。

维护者可对退出要求提出异议，并请求 TSC 决定。

<a id="maintainers-file"></a>

<a id="id6"></a>

## 10.4 MAINTAINERS 文件（MAINTAINERS File）

以下指南适用于 MAINTAINERS 文件的结构、范围与维护。

> 译注——实际文件：本文统称 MAINTAINERS 文件；本次上游对应 [MAINTAINERS.yml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/MAINTAINERS.yml)，本仓库可从[相对位置](../../../MAINTAINERS.yml)追踪。`maintainers` 和 `collaborators` 是记录领域职责的字段，编辑文件和获得 GitHub 账号权限是不同操作。

- 按 Zephyr 项目章程，应为 MAINTAINERS 文件指定负责准确性、结构和维护的人员，由 TSC 任命。

- 维护职责的划分粒度应切实可行、便于管理。

- TSC 应与现有维护者及贡献者协作，积极寻找并鼓励贡献者接管代码库中无人维护的领域，协助为这些组件指派维护者。

- 无人维护的领域必须在 MAINTAINERS 文件中明确标记。

- MAINTAINERS 文件更新应遵循：

  - 引入新文件或目录时，通常以独立提交包含相应更新。

  - 新增领域、新增维护者等重大变更，应以独立 PR 提交，并由 MAINTAINERS 文件维护者批准。这类调整可能来自将大领域拆分，或将较小领域合并。

向代码库不同领域指派维护者的指南：

架构、核心组件、子系统、示例和测试：

每个领域均须明确指派维护者。

开发板，包括相关示例和测试；以及 SoC，包括 DTS 定义：

每个开发板和 SoC 应通过一个平台领域明确指派维护者，该领域覆盖开发板、SoC 及相关组件和驱动。

驱动与后端（Drivers / Backends）

API 层面的领域须有维护者，具体驱动实现或后端也须通过覆盖该驱动实现的平台领域管理。修改驱动实例或后端时，指派驱动领域或子系统维护者。

对应官方文档源码：[doc/project/project_roles.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/project/project_roles.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../doc/project/project_roles.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未执行Git工作流、构建、发布或连接设备。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：技术指导委员会](P009_技术指导委员会.md) · [本模块主线目录](../reading/project_governance.md) · [全部主线](../reading/README.md) · [下一篇：TSC工作组](P011_TSC工作组.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P009_技术指导委员会.md) · [返回大纲](大纲.md) · [下一章](P011_TSC工作组.md)

</details>

<!-- reading-navigation:end -->
