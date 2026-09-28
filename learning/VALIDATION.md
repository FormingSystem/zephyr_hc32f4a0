<!-- SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors -->
<!-- SPDX-License-Identifier: Apache-2.0 -->

# 教学验证记录

最新补充：2026-09-27。当天先修订 Python 正文，随后重构 west 五章的正文衔接与实验交接，实验仍按“单元内实验”编排；下方旧轮次保留历史，早期独立实训入口已退休。工程环境、构建和板级实验另见[补充验收](BUILD_BOARD_VALIDATION.md)。

## 2026-09-27：west 连续阅读重构复核

以现有工作树为基线修改 west 五章及大纲，保留 30 个小节、54 个原有代码块和全部实验原件。P04 在原命令块中补入 count 缺失检查，P05 新增回到真实工程的查询块；当前共有 39 个 Bash 块，全部通过 Bash 语法检查。具体内容计数、作者冷读和通用审计候选处理见[审阅记录](REVIEW.md)。

先从 P01 新正文提取命令，在新种子 `continuity-0927-sample` 验证两仓库起点，再按五章正文顺序在 `continuity-0927-full` 执行整条路线。复用已安装且核对为 1.5.0 的 west-textbook-tools 环境，因此没有重复 P01 第一块的创建与联网安装；其余 38 个 Bash 块均执行，正文中的编辑用等价文件修改补齐。所有实验数据位于 build/learning-tools/west，缺失对照采用新的 continuity-0927-missing，未覆盖读者原有实验。

| 实验关系 | 本轮观察 |
| --- | --- |
| init 与 update | 初始化后项目未克隆；同步后应用输出 5；新窗口恢复路径仍定位同一工作区 |
| 声明与实际版本 | 只改 v2 声明时 Git 引用仍为 v1；update 后乘法可用；退回 v1 后乘法导入失败，恢复 v2 后继续 |
| 开发分支与冻结 | HEAD 多出备注提交时冻结值仍等于 manifest-rev；replay 不含备注，原分支仍可找回 |
| 清单与本地配置 | remote 重构前后的有效值相同；local/global 覆盖、guide 活动但未克隆、停用却已克隆、单次过滤均符合解释 |
| 导入边界 | self.import 文件缺失时失败，详细日志指出 missing.yml；恢复后通过；普通项目工作树改为空清单也不改变 manifest-rev 导入的 guide |
| 组练习与交接 | guide 两组只禁一组仍活动、两组都禁用则不活动；恢复直接清单后 app v1、arithmetic v2，guide 默认停用 |
| 扩展正常与失败 | count 输出 2；非法格式被拒绝；带 count 的同一实现也在缺失依赖时失败，update 后通过；禁用扩展时命令不可用，恢复后通过 |
| 新项目与交付检查 | checklist 源发布 v2 时消费方仍为 v1，修改清单后才升级；交付检查先通过，算术库手动退回 v1 时报告版本不匹配，update 后恢复 PASS |
| 返回真实工程 | 退出教学工具环境并查询工程入口，topdir 指向工程父目录，活动清单为本仓库 project-west.yml，list 只有 manifest |

第一次完整执行的验证器对导入失败消息预期过细，在 P03 缺失文件处停止。核对 west 的实际输出后补充正文详细诊断命令，并从保留现场恢复继续，直到最后的项目查询通过；没有把这一中断记作整条路线一次无错完成。预期失败均核对非零退出和对应消息，运行封装只负责断言，不替实验自动恢复。

另行执行 `check_labs.check_west`，通过 init/update、冻结重建、配置覆盖、self/project 导入、扩展正反路径，以及整套源与工作区迁移到含空格及中文路径后的回归。回归证据位于新生成的忽略目录，正文命令实跑与独立材料回归分别记录，没有相互替代。

工具采用 UCRT64 Bash、Windows Python 3.12.10、west 1.5.0 和 Git for Windows；未重新安装项目依赖。核对当前安装包的 manifest-rev 冻结实现，并对照官方 Built-in commands、West Manifests、Configuration 和 Extensions；正文仍以 1.5.0 实验结果为版本边界，不把 latest 页面当作不变的版本快照。

文档检查报告 42 份文档、16 章、13 份 Python 材料、0 错误，连续阅读严格审计五章 0 项风险。`scripts/project.py check` 的 49 项工具测试、pyOCD 离线配置检查和本地差异检查通过；验证进程显式采用 Git for Windows、MSYS2 的 sh 和 Python UTF-8，未修改系统设置。`git diff --check` 通过，文件未暂存或提交。

正文衔接为作者自行冷读，未完成外部读者试读。本轮没有执行远端发布、Linux/macOS 验证、固件构建、QEMU、图形调试或实板操作。快照、差异和完整验证日志留在忽略的 `.local/west-continuity-20260927/`。

## 2026-09-27：Python 衔接修订复核

在本仓库新建的忽略目录 `build/learning-tools/venv-continuity-o8auhusi/` 中执行 `check_labs.check_venv`，通过解释器身份、版本隔离、应用契约的成功/失败、freeze 重建、卸载隔离、约束冲突、命名遮蔽、环境级配置及可编辑安装检查。使用已有教学工具环境，构建后端为 setuptools 80.9.0；未修改根 .venv 或重新安装项目依赖。

与修改前快照对比，正文 44 个代码块完整保留；31 个 Bash 块通过 MSYS2 Bash 的语法检查，实验原件逐字节一致。本轮未重新从正文执行全部 Bash 操作，使用实际材料回归检验行为；此前整套正文顺序实跑记录仍见 2026-09-21。文档检查覆盖 42 份文档、16 章、13 份 Python 材料，报告 0 错误；连续阅读审计报告 4 章、0 风险。保留的通用审计候选及理由见[审阅记录](REVIEW.md)。

本轮没有执行 Linux/macOS、VS Code 图形调试、固件构建、QEMU 或实板操作；正文衔接由作者自行冷读，不代表已完成真实读者试读。

项目级 `scripts/project.py check` 最终通过：49 项工具测试、pyOCD 离线配置检查和本地差异检查完成。首次 PowerShell 验证进程缺少 sh 且默认编码为 GBK；补入 MSYS2 工具目录后又暴露 Git 来源混用，最终显式优先使用 Git for Windows、保留 sh 并开启 Python UTF-8 后通过。环境调整只作用于验证进程，没有修改项目配置或系统设置，日志保存在忽略的 `.local/python-continuity-20260927/project-check.log`。

## 2026-09-21：连续教材与单元内实验复核

修订公共准备章及十五篇专题正文。每章就地展示本次所需源码、命令、观察与恢复，labs 仅保存配套材料；venv/west 原综合手册改为材料索引。保持原章节 ID 与相邻导航，项目事实入口同步到新阅读路线。

从 venv 正文提取 31 个 Bash 块，在新目录顺序执行，并完成正文要求的编辑；空包、卸载、约束冲突、导入遮蔽、错误版本与可编辑源码的失败均出现对应错误并恢复。第三版构建安装成功，最终 A 与 rebuilt 的三项行为检查通过。

west 正文原有 36 个 Bash 块按新的两仓库起点顺序执行；完成清单版本、remote 等价重构、self/project import、扩展和新仓库的正文编辑。额外执行 P05 新增交付检查的两个块，实际检出偏离清单时报告 arithmetic 版本不匹配，update 后恢复 PASS。运行目录采用新的相对名称，未修改工程父工作区配置。freeze 在开发 HEAD 已前进的情况下仍对应 manifest-rev，新工作区重建符合该观察。

独立材料回归 learning/check_labs.py 仍全部通过，包括工作区整体移动到含空格、中文目录后的相对来源测试。它是维护检查，没有重新成为读者必须先运行的综合实验。

工具基线：UCRT64 Bash、Windows Python 3.12.10、pip 25.0.1、west 1.5.0、setuptools 80.9.0、Git for Windows 2.55.0.windows.3。执行日志与等价编辑保存在忽略目录 .local/textbook-validation；这些本机验证程序不属于教材前提。构建、GDB、板级与 QEMU 结果另见补充验收。

42 份文档、16 章、13 份 Python 材料的结构检查通过，章节编号、相邻链接和代码语法无错误。文字按已声明前置知识进行作者冷读，不能据此声称真实初学者试读已经通过。Linux/macOS、VS Code 图形操作和真实硬件未执行；不把命令行 GDB 或 QEMU 成功扩展为这些层次的验收。

## 2026-09-21：九篇正文的解释链与命令复核

本轮修改 venv P01—P04、west P01—P05 的实际讲解，补足任务动机、状态变化、参数选择、观察依据与恢复过程。具体阅读断点和修改位置见 [审阅记录](REVIEW.md)。两份独立实训手册仍保留，正文不再仅依靠链接跳转承担解释。

从正文提取 venv 的 26 个 Bash 命令块和 west 的 35 个可执行命令块，在新的生成目录中按章顺序执行；示意图、占位流程和用于阅读的源码片段不作为 shell 执行。所有实验路径统一换成新的相对目录名，避免复用旧环境。正文要求的清单编辑、源码字符串修改和扩展选项修改以等价编辑完成。预期失败核对非零退出码与错误内容，恢复后继续相同主线。

| 解释与操作 | 本轮观察 |
| --- | --- |
| 激活 A 后直接运行 B | 实际解释器及 prefix 属于 B，继承的 VIRTUAL_ENV 仍可属于 A |
| A/B 包版本与业务测试 | 同一代码输出 v1/v2；A 两项通过，B 两项按预期失败，pip check 仍通过 |
| 快照、约束与 pip 配置 | C 从快照重建 v1；冲突请求失败；site 值 30 与临时环境值 5 同时可见 |
| 导入遮蔽与可编辑安装 | 同名文件导致 ImportError，改名恢复；dev 修改源码后输出 edited，A 保持 v1 |
| 清单修改、同步与开发分支 | v1/v2 切换符合声明；本地提交领先 manifest-rev，普通 update 离开但保留开发分支 |
| 冻结与新工作区 | 冻结版本等于 manifest-rev 且不等于开发 HEAD，新副本按冻结取得基线 |
| remote、配置与分组 | 重构地址前后 list 输出一致；local 覆盖临时 global；停用 guide 后仍保留副本 |
| 两类清单导入 | 顶层文件拆分保留 guide；修改 app 工作树导入文件不改变 manifest-rev 中的导入内容 |
| 扩展与新仓库交付 | count 生效；非法参数、缺项目及禁用扩展均按预期失败；checklist 仅在清单接受 v2 后变化 |

venv 和 west 正文路线均完成；独立 learning/check_labs.py 回归也以 ALL CHECKS PASSED 结束。工程 check 的 49 项工具测试及 pyOCD 离线检查通过，文档检查无错误。实测纠正了正文把 west list 状态描述成布尔值的错误：它显示 active/inactive 与 cloned/not-cloned，自定义 inventory 才采用布尔值。

本轮工具基线仍为 UCRT64 Bash、Windows Python 3.12.10、pip 25.0.1、west 1.5.0、setuptools 80.9.0、Git for Windows 2.55.0.windows.3。日志与等价编辑程序保存在本机忽略目录 .local/hands-on-20260921，生成材料在 build/learning-tools 内，不作为读者前置依赖提交。

这证明本机命令路线和所检查行为成立，不等于真实初学者试读已经通过。其他系统、第三方二进制包、真实远端发布和硬件仍不在本轮实测范围；高级选项与扩展工具介绍也不冒充完整安装验证。

## 2026-09-21：按读者手册执行，而非只运行维护者脚本

本轮重写 [venv 实训](python/venv/labs/README.md)与 [west 实训](west/labs/README.md)，为每步补齐动机、参数作用、目录和状态变化、预期结果、失败定位与恢复。增加可复制的应用/requirements/unittest 模板、工作区四项验收、完整 v2 清单和计数扩展答案；原章节、专题大纲、学习中心及 project-docs 入口同步，修正“本项目没有正式 west 清单”的过期描述。

验证方法：直接提取两个手册的 15 和 21 个 Bash 命令块，在空练习目录中顺序执行。正文要求的两处编辑（修改问候语再恢复、checklist 接受 v2）以等价文件编辑完成；不是以另一套高层 API 替代读者的 pip/west 命令。故意失败的命令同时核对非零退出码和特定错误内容，恢复后再跑同一测试。随后独立运行维护者回归。

| 读者操作 | 实际证据 |
| --- | --- |
| 空 A 运行应用/测试 | 都因 lab_greeting 缺失而失败；不是跳过测试 |
| A 安装 v1、B 安装 v2 | 两份应用输出不同；A 两项通过，B 两项失败；B 的 pip check 仍通过 |
| B 降级、卸载、重装 | 降级后两项通过；卸载只让 B 缺包；A 保持通过；重装恢复 |
| freeze 与 rebuilt | 快照为 v1；新环境两项通过；直接解释器路径不依赖激活 |
| 版本约束/可编辑安装 | 矛盾约束被拒绝；Dev 改错两项失败，A 正常；源码恢复后 Dev 通过 |
| pip 环境配置 | site timeout 写入、读取 30、debug 定位及删除成功 |
| west init→update | 同一四项验收先因缺源码失败，update 后通过 |
| 清单 v2→源码同步 | 改清单后验收失败；update 后通过；回退 v1 也通过 |
| docs 分组 | 启用但未下载时失败，update 后带 --docs 的验收通过；停用后目录仍保留 |
| 自建 checklist | 完成本地源提交、标签、登记、同步；源 v2 发布后消费端保持 v1，清单接受后才改变 |
| inventory 扩展 | 新 count 对三个活动依赖返回 3；非法参数、禁用扩展均失败，恢复后正常 |
| freeze/replay | 新工作区四项通过，count=3，checklist 接受的 v2 内容一致 |
| 完整扩展答案的错误路径 | 回归在尚未下载项目时确认 count 可报告数量，而 count 加 require-cloned 必须失败 |

实测使用 UCRT64 Bash、Windows Python 3.12.10、pip 25.0.1、west 1.5.0、setuptools 80.9.0、Git for Windows 2.55.0.windows.3；额外用 MSYS2 Git 2.55.0 加 noglob 运行工作区四项验收，通过。教学工具装在 west-practice-tools，不安装进工程根 .venv。首次误用工程环境跑教学回归时缺少 setuptools 后端；切回手册规定的教学工具环境后完成回归，未为此改工程依赖。

两套实训终端记录、提取命令与审核结果保留在本机忽略的 `.local/hands-on-20260921/`；练习产物在 `build/learning-tools/venv-practice/` 和 `build/learning-tools/west/practice-01/`。它们不是教材依赖，不随 Git 交付。

维护者回归覆盖旧教程行为及新增读者测试，结果为 ALL CHECKS PASSED。工程 check 的 49 项工具测试、pyOCD 离线检查通过；文档检查覆盖 39 份文档、16 篇章节、12 份 Python 源码，错误为 0。没有改动固件源码，也没有在本轮重跑固件构建或声称新增实板验证。

连续阅读审计对两份完整手册及三篇调整章节均无风险；两份手册的首次术语检查通过。P05 原有 HEAD 被通用脚本误判为待展开缩写，正文已经明确它是 Git 当前检出引用的名称，无需编造英文全称。专题通用结构审计剩余 23 条来自既有 H1 章号和“上一篇/下一篇”标签格式，6 条来自通用 C 场景/Mermaid 建议：本仓库用 Python、Git 和真实命令验证工具行为，不为这些提示添无关 C 示例；仓库自身检查已核对链接、精确标题及相邻章节。

Linux/macOS 仅核对路径替换规则，未在对应系统实跑；未模拟全新电脑安装、远端源码托管认证或硬件操作。

## 2026-09-19 早期验收

## 实测基线

| 项目 | 本次版本 |
| --- | --- |
| 主机 | Windows 11，10.0.26200 |
| Python | 3.12.10 |
| pip | 25.0.1（该基础解释器创建环境时的版本） |
| west | 1.5.0 |
| setuptools | 80.9.0 |
| Git | UCRT64 主线为 MSYS2 Git 2.55.0；早期验证使用 Git for Windows 2.55.0.windows.3 |
| Bash | MSYS2 Bash 5.3.15，MSYSTEM=UCRT64 |

工具直接依赖写在 [requirements-tools.txt](requirements-tools.txt)。它不锁全部传递依赖；新机器若需精确保存测试环境，应额外记录安装结果和分发文件。教学脚本使用 Python 标准库以及 west 安装时所依赖的 PyYAML。

## 读者如何自行验收

当前位置：仓库根目录。UCRT64 Bash：

```bash
export MSYS="${MSYS:+$MSYS }noglob"
py -3.12 -m venv build/learning-tools/tools
build/learning-tools/tools/Scripts/python.exe -m pip install -r learning/requirements-tools.txt
build/learning-tools/tools/Scripts/python.exe -u learning/check_labs.py
build/learning-tools/tools/Scripts/python.exe learning/check_docs.py
```

自动验收要求 Python 3.11 及以上，因为文档检查使用标准库 tomllib；章节示例与种子生成器本身可使用 3.10 及以上。工具已安装时不用重复创建。不要对验收脚本使用 Python `-O`，它会关闭断言。

实验检查创建随机运行目录，不覆盖已有手工实验；成功以 `ALL CHECKS PASSED` 结束。它只在生成的独立 Git 仓库中创建教学提交，不提交本教程仓库。每次输出保留证据的位置；不自动删除，方便读者观察。检查过程中不使用用户的 west/pip 获取配置，并通过本地 wheel 安装业务依赖；可编辑安装测试在临时环境中复用已安装的构建后端文件，以免为重复检查联网下载。手工教学流程仍采用正常 pip 安装后端。

## 已覆盖的行为

| 专题 | 检查项目与可观察结果 |
| --- | --- |
| venv 身份 | 不激活时前缀不同，激活变量可为空；另核对 Bash 激活/退出及激活 A 时直接调用 B |
| 包隔离 | A/B 分别输出 v1/v2；B 卸载不改变 A；未安装时导入失败 |
| 重建与约束 | freeze 后在新环境重装；矛盾版本要求失败；pip check 通过 |
| 配置与导入 | site 配置设置/读取/删除、环境变量可见；同名文件遮蔽导致预期导入失败 |
| 可编辑安装 | 修改开发副本后新进程读取新输出 |
| west 初始化 | 本地 init 后项目未获取；update 后应用输出 5；重复种子名称拒绝覆盖；从本地清单地址以 -m/--mr 克隆初始化 |
| 版本与冻结 | 默认游离 HEAD；本地开发提交不同于 manifest-rev；冻结记录后者；新工作区按冻结重建 |
| 本地分支 | 普通 update 离开开发分支；重新 switch 后开发文件仍在 |
| 配置与组 | local 覆盖隔离的 global；启用组再更新才克隆；停用不删除目录；相对 remote/defaults 重构后地址等价 |
| 导入与扩展 | 自仓库拆分导入、普通项目导入版本边界；禁用、缺失检查、非法参数、增加计数选项 |
| 相对路径 | 整个本地实验目录移动到含空格/中文的新路径后，强制重新获取与运行仍成功 |

在项目主仓库通过 UCRT64 Bash 重新执行自动实验与主线命令。人工命令块核对与结构审阅记录在 [REVIEW.md](REVIEW.md)。

本轮同时运行 `scripts/project.py check`：使用工程原有 Python 环境及 Git for Windows 时，41 项工具测试、pyOCD 离线检查和差异检查通过。初次让工程检查使用 MSYS2 Git 时，6 项失败、8 项报错，原因是现有工程检查把 Git 输出的 MSYS 路径当作 Windows 路径。教程实验可以使用 MSYS2 Git 加准备章的 noglob 设置；工程维护检查仍沿用项目原有 Git for Windows，两者均从 Bash 发起。本次没有修改工程检查器或系统全局 PATH。

## 验证边界

UCRT64 Bash 在 Windows 本机实测；Linux/macOS 系统本身未实测，跨平台替换规则作静态核对。没有安装/验证 Zephyr SDK、硬件构建、烧录、远程 Git 认证、不同 Python 大版本或第三方带本地扩展包。主线以小型纯 Python 包验证环境隔离，不能据此推导所有平台的二进制包兼容性。

在线官方文档会更新；新特性须以安装版本帮助为准。来源与下载材料采用范围见 [REFERENCES.md](REFERENCES.md)。
