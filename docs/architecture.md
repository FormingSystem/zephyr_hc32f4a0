<!--
SPDX-FileCopyrightText: Copyright The Zephyr HC32F4A0 Contributors
SPDX-License-Identifier: Apache-2.0
-->

# 工程边界与结构

本仓库是 HC32F4A0PITB / UYUP-RPI-A-2.5 的独立开发仓库。Git 历史、工程脚本、板级依据、
调试器适配和移植代码由本仓库管理；Zephyr 内核、SDK、west 模块与厂商资料是外部依赖。
即使检出目录放在 Zephyr 源码内部，也不把本仓库文件并入 Zephyr 的 Git 历史。

## 组件关系

| 组件 | 责任 |
| --- | --- |
| `scripts/Enter-Environment.ps1` | 在当前终端定位并加载外部 Python、Zephyr、SDK 与工具 |
| `scripts/project.py` | 统一 doctor、check、build、test、debug 入口，解析工程和依赖路径 |
| `samples/bringup` | 工程自己的基础样例；当前使用 `mps2/an386` 验证编译与 QEMU 执行 |
| `zephyr/module.yml` | 本仓库作为外部 Zephyr 模块的集成入口；仅登记实际存在的组件 |
| `debug/pyocd.yaml` | HC32F4A0xI 目标、10 MHz SWD 和用户脚本配置 |
| `debug/pyocd_user.py` | 修正 pyOCD 当前目标实例的主 SRAM 地址，不访问寄存器 |
| `debug/verify_pyocd.py` | 离线验证真实配置、跨目录脚本解析、钩子时序及存储区保持 |
| `docs/hardware.md` | 唯一板级事实记录；包含用户确认、原理图映射和模板冲突 |

未来 SoC、board、DTS、Kconfig、驱动等组件仍在本仓库中实现，通过 Zephyr 的外部模块机制
接入构建。硬件尚未具备对应实现时，不用空板定义或仿真板别名冒充 HC32 支持。

## 外部依赖

Zephyr 基线为 4.4.99，提交 `f19d03c78ba70a670e3dadc2121523d33984a5c7`；
SDK 基线为 1.0.1、ARM GCC 14.3.0。构建使用 west 工作区的 CMSIS/CMSIS_6。
已有华大 `hal_xhsc` 位于外部模块，其基线提交为
`a84e04900616f68097d80cda2e89eaa8af3afadd`；当前 Zephyr 清单没有登记它。
本工程依赖记录中的 `enabled_for_hardware` 当前为 false，仿真样例不依赖该 HAL；
实现 HC32 集成时再明确启用并作为额外模块加载。

源码依赖不会复制进本仓库。其他 west 模块按实际功能补齐，不能因为基本示例能编译就认为
整个 west 工作区已同步。升级 Zephyr、SDK、CMSIS 或华大 HAL 后，重新执行构建、测试和
调试器离线验证，并更新依赖记录。

参考 PDF、DDL 压缩包与旧模板在独立资料目录保存；本文档以文件名、版本和厂商页面引用它们。
厂商代码确需导入时，先核对许可证、版本、最小导入范围与 Zephyr 构建边界，保留原始许可。

## 调试器边界

pyOCD 配置使用相对路径 `debug/pyocd_user.py`。工程入口以仓库根目录作为 `--project`，
并显式传入配置文件，因此从其他目录启动时仍能加载正确脚本。

用户钩子在 `will_init_target` 阶段修正内置 `hc32f4a0xi` 的 SRAM 元数据，发生在目标初始化
序列执行前；Flash、OTP 算法和全局内置目标定义保持原样。离线验证只用无硬件后端的探针桩，
不能证明真实 SWD、复位、烧录或时钟配置可用。
