<!--
SPDX-FileCopyrightText: Copyright The Zephyr HC32F4A0 Contributors
SPDX-License-Identifier: Apache-2.0
-->

# 移植状态

记录日期：2026-09-09。目标为 UYUP-RPI-A-2.5 的 HC32F4A0PITB，12 MHz 外部晶振、
2 MiB Flash、512 KiB 主 SRAM。工程当前处于独立仓库与开发组件建立阶段。

| 项目 | 状态与证据 |
| --- | --- |
| 主机编译环境 | 已核验 Zephyr 4.4.99、SDK 1.0.1、GCC 14.3.0、Python 3.12.10、west 1.5.0、CMake 4.4.3 |
| 外部 Zephyr 基础验证 | `mps2/an386` 的 hello_world 构建与 QEMU 输出成功；Twister 1/1 通过 |
| 工程依赖检查 | `project.py doctor` 通过 Zephyr 模块 schema、锁定的 Zephyr/SDK/CMSIS_6/pyOCD 版本检查 |
| 板卡资料 | 已核对单页原理图与厂商引脚表，用户确认 12 MHz、NC 和板载 DAP 操作；见 hardware.md |
| pyOCD 工程配置 | 使用 hc32f4a0xi、10 MHz SWD、禁用自动解锁擦除，修正主 SRAM 地址 |
| pyOCD 离线验证 | 真实 Session 跨目录加载相对脚本、真实初始化钩子与重复调用通过；Flash/OTP 算法、备份 RAM、全局目标图保持不变 |
| 工程工具检查 | `project.py check` 通过 5 项真实 Git 工具测试与 pyOCD 离线检查；CMake/Kconfig 风格检查通过 |
| 工程基础样例 | `project.py build` 构建 samples/bringup / mps2/an386 成功，Flash 19356 B、RAM 6440 B |
| 工程运行测试 | `project.py test` 执行本仓库样例，Twister 1/1 通过、零警告，耗时 18.26 秒 |
| CI 配置 | 已有 GitHub Actions 工具检查矩阵；尚未在远端执行 CI |
| HC32 SoC、board 与驱动 | 尚未实现，不能构建 HC32 Zephyr 固件 |
| 实板调试与运行 | 未完成；此前主机只读枚举未发现可用调试探针 |

外部 hello_world 历史验证与本仓库 samples/bringup 分别执行过构建与运行测试。
本仓库验证命令如下：

```powershell
python scripts/project.py doctor
python scripts/project.py check
python scripts/project.py build
python scripts/project.py test
python debug/verify_pyocd.py
```

本地结果日志为 `build/project-check.log`、`build/project-build.log`、`build/project-test.log`；
编译产物在 `build/bringup`，Twister 结构化结果在 `build/twister`。这些文件不受版本控制。

## 首轮移植顺序

1. 根据官方设备定义建立 SoC、Flash/SRAM 布局、启动与异常/中断入口。
2. 建立 12 MHz 时钟路径，校验 PLL、Flash 等待周期、总线时钟和 SysTick。
3. 实现必要的 GPIO、pinctrl、USART1 控制台及中断源路由。
4. 建立 UYUP-RPI-A-2.5 板级 DTS/Kconfig/CMake 与 pyOCD runner；蓝灯 PD10 低有效。
5. 接板验证 SWD、SRAM、复位、LED3 和 115200 8N1 串口，再扩展外设。

原理图中的通用芯片符号、24 MHz 旧模板和其他板卡 BSP 不能直接作为本板实现。
硬件事实统一维护在 [hardware.md](hardware.md)，工程边界见 [architecture.md](architecture.md)。

## 尚未验证

尚未对实板进行时钟测量、连接、复位、Flash 擦写、下载或 Zephyr 运行测试；
未完成完整 Zephyr 上游合规检查，也未声称所有 west 模块已同步。
离线调试检查不访问目标寄存器；QEMU 通过不构成 HC32 硬件通过。
