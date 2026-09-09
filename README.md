<!-- SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors -->
<!-- SPDX-License-Identifier: Apache-2.0 -->

# zephyr_hc32f4a0

HC32F4A0PITB / UYUP-RPI-A-2.5 的 Zephyr 外部移植模块和工程工具。
本仓库保存自研组件，Zephyr 内核、SDK 和厂商 HAL 作为外部依赖使用。

当前具备独立 Git 框架、模块入口、bring-up 示例、构建/测试工具和 pyOCD 调试配置。
示例以 `mps2/an386` 验证主机工具链和模块接入；HC32 SoC、开发板与硬件驱动尚待实现。

## 在当前工作区开始

在本仓库根目录的 PowerShell 中执行：

```powershell
. .\scripts\Enter-Environment.ps1
python scripts/git_setup.py
python scripts/project.py doctor
python scripts/project.py check
python scripts/project.py build
python scripts/project.py test
```

入口会使用现有 west 工作区的 Python 虚拟环境和 Zephyr SDK，然后停留在本仓库根目录。
构建与测试输出均放在本仓库 `build/` 中。工具不会自动下载依赖、推送提交或擦除芯片。

## 工程组成

| 位置 | 职责 |
| --- | --- |
| `zephyr/module.yml`、根 CMake/Kconfig | Zephyr 外部模块入口与搜索根 |
| `soc/`、`boards/`、`dts/`、`drivers/` | 后续 HC32 SoC、UYUP 板卡、设备树与外设实现 |
| `samples/bringup/` | 可运行的控制台/心跳示例，兼容后续实板启动 |
| `debug/` | 10 MHz SWD 配置、HC32 SRAM 映射修正与离线验证 |
| `scripts/` | 本地 Git 配置、环境发现、工程命令与提交校验 |
| `tests/tooling/` | Git 钩子与工程工具测试 |
| `governance/` | 从 linux-note 继承并适配的 Git 协作框架 |

- [开发与调试](docs/development.md)
- [组件架构](docs/architecture.md)
- [硬件事实与板卡操作](docs/hardware.md)
- [移植状态](docs/porting-status.md)
- [Git 规范](governance/conventions/git_guide.md)
- [框架来源与适配范围](governance/architecture/framework_provenance.md)

## 依赖与许可

固定依赖基线见 [dependencies.lock.json](dependencies.lock.json)。Python 工程工具依赖见
[requirements-tools.txt](requirements-tools.txt)；Zephyr 构建依赖仍按其源码中的 requirements 安装。
激活脚本按并列布局定位同级 `zephyr/` 源码目录，也可通过 `ZEPHYR_BASE`、`VIRTUAL_ENV` 和
`ZEPHYR_SDK_INSTALL_DIR` 使用其他已准备好的本机工作区。

本项目新增实现采用 Apache-2.0；直接继承自 linux-note 的治理文件和钩子保留其
GPL-2.0-only 许可与来源说明。第三方 Zephyr、HAL 和资料不复制进本仓库。
