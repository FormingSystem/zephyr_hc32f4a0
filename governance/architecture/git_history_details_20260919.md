<!-- SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors -->
<!-- SPDX-License-Identifier: Apache-2.0 -->

# 2026-09-19 Git 历史明细补充记录

开发者明确要求为全部历史提交补充换行的 `- 详情` 列表。本次据此执行本地自有历史的消息迁移，
并将今后的项目提交规则收紧为至少一条具体列表正文。原规则允许只有标题，是此前多条消息没有正文的直接原因。

## 迁移范围与保留项

检查全部 6 个本地分支可达的 19 条自有提交：11 条缺正文，8 条已有正文。
11 条按各自提交当时的文件改动与文档记录补充，已有 8 条消息原样保留。
祖先变化使 14 个提交对象取得新标识；前 5 个对象未变。没有拆分、合并或新增历史提交。

四个本地分支引用发生变化：master、content/learning-foundations、docs/intro-guide、
fix/git-rule-inheritance；另两个分支指向的早期节点未变。引用用带预期旧值的事务一次更新。

每对新旧节点的 tree 相同，原始作者、提交者、时间、时区及其他非 parent 头字段逐字相同。
没有用当前测试结果冒充历史测试，也没有改历史文档里的旧提交号；旧号仍代表当时的记录，可通过下表追溯。
迁移时索引字节、未暂存差异、未跟踪路径和全部已备份文件内容一致；没有清空或顺便提交此前未提交的教学工作。

## 备份与校验

迁移前完整 bundle 位于本机忽略目录 `.local/git-details-20260919/all-before-rewrite.bundle`，
大小 146004243 字节，已执行 git bundle verify：

```text
SHA-256: 5d959d95e63ec7a11845a0ea8e2b68baad1500919ca98fc913721b9a682558ef
```

同目录保存 before.json、94 个工作区候选文件的 worktree-before.zip、原始索引、暂存/未暂存补丁、
消息草稿、mapping.json、reference-transaction.txt 与 result.json。备份不提交。
恢复时先读映射和备份，不用 reset --hard 覆盖仍在工作的目录；可在独立目录克隆 bundle 只读检查旧历史。

## 新旧节点对照

| 原节点 | 当前本地节点 | 消息处理 |
| --- | --- | --- |
| `c44dd1bd4c6abdf71e5af542088ec9a30e3593ae` | `c44dd1bd4c6abdf71e5af542088ec9a30e3593ae` | 原消息保留 |
| `fb2fe5a0a7678651699aa21ed2bbb1b1a7f1614d` | `fb2fe5a0a7678651699aa21ed2bbb1b1a7f1614d` | 原消息保留 |
| `9aebb8f6daf82e4d87cb56a355f276fabdede055` | `9aebb8f6daf82e4d87cb56a355f276fabdede055` | 原消息保留 |
| `fd79985e1bf6bbfa2a101e95c555194070002cad` | `fd79985e1bf6bbfa2a101e95c555194070002cad` | 原消息保留 |
| `388f616e754f8e6a9150d54cd3f16fbe82e9fe6e` | `388f616e754f8e6a9150d54cd3f16fbe82e9fe6e` | 原消息保留 |
| `8cb8a613797ffb48e3af1d4cad162f30b3a3c6ae` | `d38fb520a05aecbe12999f6e1ad8e21f1e5a3551` | 补充具体列表明细 |
| `712466f3ac9fd88cebf96e75747ba1f919886be1` | `734b10151133a1af6cf67e24dd8777926464802b` | 补充具体列表明细 |
| `f66f25596de9dbe158f5de9874044512125a4ba7` | `9bd610d6b66db90a34d18bdb411306e66f7c383f` | 补充具体列表明细 |
| `3f6d306aceb3cf74245ea7508cab9488363de635` | `22f2daf12a4e71610886173ee968bd324123ce2d` | 原消息保留 |
| `2f08075a56c84daf73f4031184f547d96d47d3b0` | `a523919275ad7ce16634872d5ec2d80e6772284b` | 原消息保留 |
| `d02d4638473bb9082fa17b128c1dd3ab5b00495d` | `742d3d7ddec5d1357d63b5fff685fca853f50e52` | 原消息保留 |
| `11f8883ecc5ea1b13b9af079515a9ec622acf602` | `921dfa6f7c5bed7acf41b35005c304cf8fa31cdc` | 补充具体列表明细 |
| `d9d844079a47661086c0d84033d25d65be2efd1a` | `283b090cfaf3f8487b1e83df138dbc476a7d6710` | 补充具体列表明细 |
| `1374639edbd36d8956e85f8e855c281621417f82` | `e61d943def3c2346d9122e3660d45b762923b755` | 补充具体列表明细 |
| `95d99c528542f83adafdb5133f1dc6a87e2a8ffc` | `bbccf4b9244adca9f92a8fa27699331562b1785a` | 补充具体列表明细 |
| `d6aa77dff3df37bdb51dd1198a5024b26bd06d5b` | `d77ac06d8694a19d7435a1e054050cea8141d96f` | 补充具体列表明细 |
| `846d264219e91e1cc04f3b948645206827d7bc78` | `81a84bf98bee4cf00001d20d3ec70f6fc4010fda` | 补充具体列表明细 |
| `08914165d3045cde13dc9a1b3d8f8049feb19a2e` | `e49fab634e955eeb954a0137ad809850196c8ff5` | 补充具体列表明细 |
| `4a26efd18f972d705d130f887df932f86325fe60` | `4c2383f76066d24e8595125b27932178c5d4c8f7` | 补充具体列表明细 |

## 当前规则与验证

[Git 规范](../conventions/git_guide.md)、AGENTS 和提交模板已同步为强制正文。
当前 .githooks/commit-msg 先执行 upstream/commit-msg 的来源格式校验，再拒绝只有标题、
只有注释或空白明细的消息。原始来源钩子和模板保存在各自 upstream 目录，原文摘要保持不变，
继承关系见[框架来源](framework_provenance.md)。

19 条当前历史消息逐条通过当前严格钩子；49 项工程工具测试、pyOCD 离线检查和差异检查通过。
Git 工作流回归同时确认“来源原实现仍允许单标题”和“本项目入口拒绝单标题”，避免混淆来源与项目覆盖。
源码文件树没有因消息迁移发生变化，本次未重复构建固件或操作硬件。

完成历史改写时，规则、回归和本说明仍为工作区修改；其后按开发者要求与教学工作分别组织提交，归档状态见项目记录。

## 远端与旧克隆

本次没有推送；origin/master 仍保留迁移前的 `4a26efd18f972d705d130f887df932f86325fe60`。
远端跟踪引用和 Dependabot 分支均未改写，因此 `git log --all` 仍能显示旧链和机器人提交。
核对本次结果使用 `git log master --format=full`；不能把远端旧链继续显示误认为本地明细没有生效。

第一次迁移结束时本地主线为 `4c2383f76066d24e8595125b27932178c5d4c8f7`，最终节点见下方再次修正记录。未来获明确推送指令时，先重新核对远端，
仅针对授权的分支使用精确旧值的 --force-with-lease；远端已变化则停止，不能镜像推送或覆盖机器人分支。
在发布迁移前，不直接把旧 origin/master 合并回新 master，否则会重新混入旧链。

## 再次修正：正文改为面向维护者的修改总结

开发者指出前次正文仍偏向文件与操作罗列，未清楚表达修改意义。本次重新审阅 19 条自有提交，
正文围绕当时解决的问题、采取的改动和行为变化重写，去掉文件清单与无助于理解变化的检查流水账。
标题、文件树、作者/提交者与时间保持不变；本次 19 个对象及 6 个本地分支引用更新。

上方表格和统计描述第一次补明细的过程；下表是该过程之后的再次修正。前述“已有 8 条消息保留”
只适用于第一次迁移，最终这 8 条也已重新审阅并重写正文。当前主线为
`9836f28d9b3950088f61cf654f6364caa904d979`。

再次改写前的完整备份位于 `.local/git-summaries-20260919/all-before-rewrite.bundle`，已通过 bundle verify；
SHA-256 为 `1298d57c3be5c83e1d3498b7a03cbfcbb85a90389589cdf4a5675d2f33d01aa8`。
同目录保存 103 个工作区候选文件、原索引、补丁、消息与映射。迁移前后逐字核对工作区与索引，结果一致。
19 条最终消息逐条通过当前钩子；语义由逐条审阅确认，钩子不能判断总结是否写得有用。

| 第一次补明细后的节点 | 最终修改总结节点 |
| --- | --- |
| `c44dd1bd4c6abdf71e5af542088ec9a30e3593ae` | `c78f689f9a57651ed98026b5a07d8d5029222877` |
| `fb2fe5a0a7678651699aa21ed2bbb1b1a7f1614d` | `1e2cc65b868bedfd5e50aa7d40b2f8a994fdcb21` |
| `9aebb8f6daf82e4d87cb56a355f276fabdede055` | `dd07838808bafe400a35a34fcefcb2e9981e4025` |
| `fd79985e1bf6bbfa2a101e95c555194070002cad` | `af03682ccadbf2f2588777658a129f594fbb0ece` |
| `388f616e754f8e6a9150d54cd3f16fbe82e9fe6e` | `070821bd0a17a72dc28b47fd44404b76b980448e` |
| `d38fb520a05aecbe12999f6e1ad8e21f1e5a3551` | `65cc64fc16d3013c51c05ded845ec4e6ea6e1212` |
| `734b10151133a1af6cf67e24dd8777926464802b` | `aa0f5b836fe4a5be9c6c705946e7373e2b46392d` |
| `9bd610d6b66db90a34d18bdb411306e66f7c383f` | `9086311df9ae11109718f847f9aee3ee99cf1d3b` |
| `22f2daf12a4e71610886173ee968bd324123ce2d` | `0bc6a4074b60075e449bb84f5e7bcee8cc222b1b` |
| `a523919275ad7ce16634872d5ec2d80e6772284b` | `2956837d88b80c15ab8100e0435aec1ac042d015` |
| `742d3d7ddec5d1357d63b5fff685fca853f50e52` | `4c372c13464ba82938f7842e65904bde65528312` |
| `921dfa6f7c5bed7acf41b35005c304cf8fa31cdc` | `2ae5f1a76326b5264dad511ffd029b1fb70fb3ea` |
| `283b090cfaf3f8487b1e83df138dbc476a7d6710` | `4fa1b1157f03a4711bec0808b1733bb770e5402f` |
| `e61d943def3c2346d9122e3660d45b762923b755` | `46b6497fbfff707bc88e5dc3bb6149db27b76b4f` |
| `bbccf4b9244adca9f92a8fa27699331562b1785a` | `e79019b877d48c5810c1f94a96d70d3d73ed17da` |
| `d77ac06d8694a19d7435a1e054050cea8141d96f` | `f78a20059bd30871f7ff24505b8009f49cc656fa` |
| `81a84bf98bee4cf00001d20d3ec70f6fc4010fda` | `ae3857ffa86d7916a350e207452a3a763a7919a2` |
| `e49fab634e955eeb954a0137ad809850196c8ff5` | `cf8e4744d677b2c9c9d705b7d9474bfe355c6d57` |
| `4c2383f76066d24e8595125b27932178c5d4c8f7` | `9836f28d9b3950088f61cf654f6364caa904d979` |

此次也未推送远端，原远端节点与机器人分支保持不变。后续推送仍需重新核对远端并使用精确 lease。

## 经授权推送结果

开发者随后明确要求强制推送远端。重新核对远端 master 仍为
`4a26efd18f972d705d130f887df932f86325fe60`，完整 bundle 再次校验通过后，
以该旧值作为精确 `--force-with-lease` 条件，仅更新 origin 的 master。
推送成功；再次用 ls-remote 核对远端为 `9836f28d9b3950088f61cf654f6364caa904d979`，
与本地 master、origin/master 一致。以上各节“未推送”描述的是获得本次授权之前的状态。
本次推送只发布已改写的提交历史，工作区尚未提交的教程和规则修改未包含在内。
