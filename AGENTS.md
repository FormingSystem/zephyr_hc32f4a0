<!-- SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors -->
<!-- SPDX-License-Identifier: Apache-2.0 -->

# 项目协作约定

本项目的独立开发仓库名为 `zephyr_hc32f4a0`，远程为
`git@github.com:FormingSystem/zephyr_hc32f4a0.git`。
执行任何 Git 写操作前，核对 `git rev-parse --show-toplevel` 和远程地址，确认操作的是当前项目克隆。
本机开发目录与官方源码参考目录的确切位置见下方私人环境配置；官方参考目录不是本项目的构建依赖。
本仓库直接包含完整 Zephyr 源码，以及构建 HC32 所需的 CMSIS_6、厂商 HAL。
单独 clone 本仓库后应能使用已安装工具链构建，不能偷偷回退到旁边的官方目录。

先读 `README.md`、`project-docs/architecture.md`、`project-docs/hardware.md` 和
`governance/conventions/git_guide.md`。硬件事实以 `project-docs/hardware.md` 为唯一项目记录。

## 私人环境配置（仅本机，不纳入 Git）

新窗口开始工作时，若 [私人环境配置](.local/PRIVATE_ENVIRONMENT.md) 存在，先读取它确认本机目录、
工具位置、芯片资料缓存和厂商示例入口。这个链接指向本机私人配置文档，不是可移植的公共开发说明。

- `.local/PRIVATE_ENVIRONMENT.md` 和 `.cache/` 均由 Git 忽略；私人文档与资料本体不暂存、不提交。
- 芯片手册、厂商 DDL 和示例缓存在 `.cache/hc32f4a0/`，具体来源、版本、文件校验及检索入口在私人配置中。
- 缓存用于核对实现和依据，不作为构建依赖。新克隆没有私人文件或缓存是正常情况，公共构建入口仍按 README 执行。
- 参考示例的评估板、晶振、封装和中断框架可能与本项目不同；移植结论核对后写入公共硬件记录和受控源码。

## 工程边界

- 本仓库是完整 Zephyr 源码工程，板级与 SoC 支持直接集成到树内，使用硬件模型 v2。
- 所有自研板级支持、SoC、设备树、驱动、示例、工具和文档都在本仓库中维护。
- Zephyr、CMSIS 和厂商 HAL 源码纳入版本控制；SDK/Python 是外部主机工具。
  源码基线见 `dependencies.lock.json`，导入代码保留原许可证；不要提交依赖仓库的 `.git`。
- 构建产物仅进入被忽略的 `build/`，本机配置进入 `.local/`，外部参考资料进入 `.cache/`。不得提交绝对路径、
  虚拟环境、缓存、固件产物、凭据或未经确认许可的资料。
- 厂商 HAL 的集成修正在树内 SoC/驱动中处理；不修改已安装的 Python 包。
- 不能创建虚假的可用 HC32 board/SoC，也不能把 QEMU 成功称作 HC32 实板验证。
- 工程介绍、移植记录和 Zephyr 学习资料维护在 `project-docs/`，目录入口为 `project-docs/README.md`。
- 系统学习与实验按 [专题蓝图](project-docs/learning/专题蓝图.md) 分批建设，执行
  [实验约定](project-docs/learning/实验规范.md)。阅读入口只登记真实文章；文档、构建、模拟运行和实板验证分别记录状态。
- 每次交付更新 `project-docs/porting-status.md`，记录完成范围、验证方法与尚未执行的硬件步骤。

## 硬件约束

- HC32F4A0PITB，LQFP100，2 MiB Flash、512 KiB 主 SRAM，另有 4 KiB 备份 SRAM。
- 主 SRAM 从 `0x1FFE0000` 开始；12 MHz 实装晶振，PLL、总线和 Flash 等待周期必须重算。
- 芯片没有的引脚按 NC 处理；通用兼容原理图的符号名不能替代 HC32 物理脚号。
- 板载 CMSIS-DAP 默认 2.x / WinUSB，支持 10 MHz SWD；一根 USB 可调试和输出串口。
- 使用外部探针前按硬件文档停用板载 DAP。BOOT 擦除是恢复步骤，不是日常构建或检测动作。

## 代码与 Git

- C、Kconfig、CMake 和设备树遵循当前 Zephyr 对应风格规范；新文件保留 SPDX。
  具体规范见 `doc/contribute/style/`；上游原文件的许可证和作者记录保持不变。
- Git 规则继承 linux-note 的固定来源节点，完整规则与核对范围见
  [Git 规范](governance/conventions/git_guide.md)和[继承记录](governance/architecture/framework_provenance.md)。
  不得自行简化规则、添加尾注例外，或仅以钩子通过代替规则审查。
- 提交标题使用 `<类型>[(项目[/模块])]!?: <中文结果>`。知识正文/研究内容用 `content`，
  使用说明/设计/治理文档用 `docs`；其他类型按规范的用途选择，不能按文件后缀分类。
- 范围语法可选，允许任意语言的一到两层，不设范围白名单。需要定位归属时，按照本次修改的真实对象自由填写；
  变更横跨整个仓库且不存在准确范围时可以省略。语法允许省略范围不代替对实际归属和提交粒度的审查。
- 一个提交只形成一个可独立审查和回退的结果。实现所需测试与文档随实现；独立治理政策、
  知识内容和发布动作分别提交，不按扩展名分组，也不因用户说“全部提交”就合并无关结果。
- 标题能表达单一结果时不强加正文；需要正文时，每个非空非注释行使用 `- 描述`。
  继承的钩子不接受独立 `Assisted-by`、`Signed-off-by` 或 `Co-authored-by` 尾注；不得代造人工签署。
- 主线为 `master`，只接受验证通过的快进更新。已交付或推送历史用 revert 撤销，不擅自改写。
  只有开发者明确授权的仓库级历史迁移，才可在创建并验证完整 bundle 备份后使用 `--force-with-lease`。
- 明确列出暂存路径并检查暂存区。本项目附加的执行限制：禁止 `git add .`、`git add -A` 或提交依赖仓库。
- 日常提交保持已有历史中的作者、签署和提交消息原样；显式授权的历史迁移按上方备份与保护约定执行。
  已完成的授权迁移见[历史记录](governance/architecture/git_history_repair_20260911.md)。不得在提交中声称未执行的硬件验证。
- 本地初始化使用 `python scripts/git_setup.py`；检查使用 `python scripts/project.py check`。
  修改模块或示例后再运行 `python scripts/project.py build` 和 `python scripts/project.py test`。
- 本项目附加的发布约定：未获推送指令时只建立和验证本地提交，不自动发布到远端。
