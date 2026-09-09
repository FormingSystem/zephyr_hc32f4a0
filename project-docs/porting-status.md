<!--
SPDX-FileCopyrightText: Copyright The Zephyr HC32F4A0 Contributors
SPDX-License-Identifier: Apache-2.0
-->

# HC32F4A0PITB 移植状态

验证日期：2026-09-09；文档更新：2026-09-10。板卡 UYUP-RPI-A-2.5，目标 `uyup_rpi_a/hc32f4a0pitb`，
LQFP100、2 MiB Flash、512 KiB 主 SRAM。已实现首轮可构建的移植；实板运行尚未验收。

工程文档目录已统一为 `project-docs/`，用于工程介绍、移植记录和 Zephyr 学习资料；
导航见 [文档入口](README.md)。本次调整更新目录与引用，38 个本地 Markdown 链接和 Git 差异检查通过；
未重新执行固件构建，既有构建和硬件验证状态不变。

## 工程与源码节点

仓库根目录包含完整 Zephyr 源码快照，以及 HC32 需要的 CMSIS_6、华大 HAL。
不依赖同级官方源码，不导入上游 Git 历史，SDK、虚拟环境与构建产物不提交。
准确基线见 [source-baseline.md](source-baseline.md) 和
[dependencies.lock.json](../dependencies.lock.json)。

导入清单核对：Zephyr 66244 个受控源文件、CMSIS_6 793 个、HAL 224 个，零缺失。
CMSIS_6/HAL 的文件内容与基线一致；Zephyr 已有文件仅修改工程治理配置、
GPIO/UART 的 CMake/Kconfig 接入及厂商前缀，其余移植采用新增文件；LICENSE 仅清理末尾空行。
源文件合计 340132030 字节，约 324.4 MiB，不含 Git 历史或工具安装。

## 已实现的目标能力

| 项目 | 实现 |
| --- | --- |
| SoC / board | 硬件模型 v2；Cortex-M4F、144 个外设 IRQ 槽、4 位 NVIC 优先级 |
| 启动与链接 | Zephyr 原生启动/向量，项目复位钩子正确返回；ICG 固定 `0x400..0x45f` 并保留、断言长度 |
| 存储布局 | Flash `0x00000000` / 2 MiB；SRAM `0x1FFE0000` / 512 KiB；备份 SRAM 不并入主内存 |
| 时钟 | PH0/PH1 的 12 MHz XTAL 直接驱动 CPU/总线，DIV1，Flash/SRAM 0 wait；PLLH/PLLA 关闭 |
| 时钟启动 | MRC 仅作过渡；等待晶振稳定，失败 panic，不以 RC 冒充 12 MHz |
| 控制台 | USART1，PA9/PA10，115200 8N1；polling 输入、输出、错误检查 |
| GPIO | 输入、推挽/开漏输出、上拉、端口读写/toggle；拒绝 NC、下拉与尚未支持的中断模式 |
| 板级信号 | PD10/PE15 低有效 LED；PA3/PE2 按键轮询；LQFP100 未引出脚由保留范围与驱动掩码排除 |
| pyOCD | 2 MiB Flash 目标、10 MHz SWD、修正 SRAM 起点、禁止自动解锁擦除 |
| VS Code | 单一项目根展示完整源码；自动终端环境；默认构建 HC32，成功后自动审计镜像 |

MRC 本身的容差不适合保证串口精度，因此只作启动过渡，工作时钟使用板载晶振。
12 MHz 下 USART 分频的理论量化误差约 +0.03%；这不是串口实测结果。

## 已执行验证

| 验证 | 结果 |
| --- | --- |
| 原生 CMake/Ninja HC32 全新构建 | 成功，编译器与 CMake 零警告；Flash 25552 B，RAM 4224 B |
| 独立克隆构建 | 对 `b0bd5ee270042dcd2b007ad0d65025e1a8629ead` 执行 `git clone --no-local` 到外部新目录；doctor、全新 HC32 构建与自动镜像审计通过，内存占用相同 |
| ELF/配置审计 | HC32 board、Flash/SRAM 边界、160 项向量表、初始 SP、Thumb reset 地址、ICG 值均通过 |
| 源码来源审计 | 117 个编译单元全部在项目内，18 个显式头文件路径限于项目/SDK/Python，CMSIS_6 位于项目内 |
| 审计反例 | 损坏 ICG、初始 SP、复位向量或将编译源指向外部 Zephyr 时均失败退出 |
| 工具回归 | 23 项 Git/目录/命令/快照差异测试通过，包括源隔离、编译失败不审旧镜像、审计失败传播 |
| pyOCD 离线检查 | 真实 Session 跨目录加载配置/脚本，修正局部 SRAM，不打开探针；通过 |
| QEMU 软件回归 | 本仓库 Twister：2 个场景中 HC32 编译场景被过滤，MPS2 运行 1/1 通过，零警告，20.19 秒 |
| 源码风格 | SoC CMake/Kconfig 风格、UART/GPIO clang-format 检查通过 |

独立克隆位于原 west 工作区之外，未复制本机配置或原构建缓存，只显式使用已安装的 SDK 与 Python 环境。
启动前故意设置无效的外部 `ZEPHYR_BASE`、`ZEPHYR_MODULES` 和 `EXTRA_ZEPHYR_MODULES`，
工程入口均正确覆盖或清除；117 个编译单元全部来自克隆目录，18 个显式头文件搜索路径审计通过。
该次 ELF SHA-256 为 `ce36b09374597eff863c546f9a0c54d8b78108f85652154a2eb47a44e70eb411`。
这验证了受控文件的独立构建完整性；新机器自动创建虚拟环境的 Setup 脚本已做语法检查，尚未实跑重装工具依赖。

```powershell
. ./scripts/Enter-Environment.ps1
python scripts/project.py doctor
python scripts/project.py check
python scripts/project.py build --pristine
python scripts/verify_hc32_image.py
python scripts/project.py test
```

本机结果在被忽略的 `build/hc32-build.log`、`build/hc32-image-audit.json`、
`build/qemu-test.log`、`build/standalone-build.log`、`build/twister/`，ELF/HEX/BIN 在 `build/bringup/zephyr/`。
镜像审计记录 ELF SHA-256，以便对应具体构建，重编后以最新审计为准。

## 待实板验收与后续扩展

尚未执行目标连接、复位、Flash 擦写、下载、晶振/时钟测量、串口回显或 LED 实测。
编译和 QEMU 通过不等于 HC32 实板通过。完整 Zephyr 上游合规与远端 CI 尚未执行。

下一步接 USB2/DAP，核对探针/串口枚举，验证 SWD、晶振起振、SysTick、115200 控制台和 LED。
再增加外设中断源路由、UART 中断/DMA、GPIO 中断、时钟/引脚框架、Flash 驱动及其他外设。
MPU 暂不启用：主 SRAM 起点不满足单个 512 KiB MPU 区域对齐，需要分区设计。
PLL 提频需要单独核对 12 MHz 输入、VCO、总线、Flash/SRAM 等待与实测，不复制旧 24 MHz 模板。
硬件事实与板载 DAP 操作持续以 [hardware.md](hardware.md) 为准。
