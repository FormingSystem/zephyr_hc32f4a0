<!-- SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors -->
<!-- SPDX-License-Identifier: Apache-2.0 -->

# 项目协作约定

本项目的独立开发仓库是 `G:\zephyr\zephyr_hc32f4a0`，远程为
`git@github.com:FormingSystem/zephyr_hc32f4a0.git`。本段绝对路径仅用于本机工作树发现。
执行任何 Git 写操作前，核对 `git rev-parse --show-toplevel` 指向本仓库。
同级目录 `G:\zephyr\zephyr` 是独立的 Zephyr 源码依赖。两个仓库并列，
不在 Zephyr 的索引中添加本项目，也不在其源码目录内开发本项目组件。

先读 `README.md`、`docs/architecture.md`、`docs/hardware.md` 和
`governance/conventions/git_guide.md`。硬件事实以 `docs/hardware.md` 为唯一项目记录。

## 工程边界

- 本仓库通过 `zephyr/module.yml` 向 Zephyr 提供外部模块；使用硬件模型 v2。
- 所有自研板级支持、SoC、设备树、驱动、示例、工具和文档都在本仓库中维护。
- Zephyr、SDK、CMSIS 和厂商 HAL 是外部依赖；版本基线见 `dependencies.lock.json`。
- 构建产物仅进入被忽略的 `build/`，本机配置进入 `.local/`。不得提交绝对路径、
  虚拟环境、缓存、固件产物、凭据或未经确认许可的资料。
- 不修改厂商 HAL 或已安装的 Python 包来绕过问题；项目适配放入本仓库。
- 不能创建虚假的可用 HC32 board/SoC，也不能把 QEMU 成功称作 HC32 实板验证。
- 每次交付更新 `docs/porting-status.md`，记录完成范围、验证方法与尚未执行的硬件步骤。

## 硬件约束

- HC32F4A0PITB，LQFP100，2 MiB Flash、512 KiB 主 SRAM，另有 4 KiB 备份 SRAM。
- 主 SRAM 从 `0x1FFE0000` 开始；12 MHz 实装晶振，PLL、总线和 Flash 等待周期必须重算。
- 芯片没有的引脚按 NC 处理；通用兼容原理图的符号名不能替代 HC32 物理脚号。
- 板载 CMSIS-DAP 默认 2.x / WinUSB，支持 10 MHz SWD；一根 USB 可调试和输出串口。
- 使用外部探针前按硬件文档停用板载 DAP。BOOT 擦除是恢复步骤，不是日常构建或检测动作。

## 代码与 Git

- C、Kconfig、CMake 和设备树遵循当前 Zephyr 对应风格规范；新文件保留 SPDX。
- 本仓库提交语法继承 linux-note：`<类型>[(项目[/模块])]!?: <中文结果>`；
  正文按需使用 `- ` 列表，规则和来源见 governance 文档。
- 主线为 `master`，只接受验证通过的快进更新。已交付历史用 revert，不 reset 或强推。
- 明确列出暂存路径并检查暂存区。禁止 `git add .`、`git add -A` 或提交依赖仓库。
- 代理创建的提交包含一个 `Assisted-by` 尾注；不添加 `Signed-off-by` 或 `Co-authored-by`。
  人工签署的有效尾注不得删除。不得在提交中声称未执行的硬件验证。
- 本地初始化使用 `python scripts/git_setup.py`；检查使用 `python scripts/project.py check`。
  修改模块或示例后再运行 `python scripts/project.py build` 和 `python scripts/project.py test`。
- 未获推送指令时只建立和验证本地提交，不自动发布到远端。
