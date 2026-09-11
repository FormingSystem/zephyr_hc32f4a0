<!--
SPDX-FileCopyrightText: Copyright The zephyr_hc32f4a0 Contributors
SPDX-License-Identifier: Apache-2.0
-->

# 完整源码工程结构

本仓库在一个源码根目录中维护 Zephyr 与 HC32F4A0PITB 移植。编译时 `ZEPHYR_BASE` 指向
本仓库根目录，CMSIS_6 和华大 HAL 也从本仓库读取；不依赖旁边的官方源码目录。
Git 历史由本工程独立维护，导入的是源文件快照，不包含上游 Git 对象或历史。

```text
zephyr_hc32f4a0/
├── kernel/ arch/ include/ subsys/ cmake/   Zephyr 完整核心源码
├── soc/xhsc/hc32f4a0/                    HC32 SoC 适配
├── boards/uyup/ dts/arm/xhsc/            板卡和设备树
├── drivers/                             Zephyr 驱动与 HC32 GPIO/USART
├── modules/hal/cmsis_6/                  CMSIS_6 源码
├── modules/hal/xhsc/                     华大 HAL 源码
├── samples/bringup/                     板卡启动示例
├── samples/learning/ tests/learning/    课程实验与自动化用例
├── scripts/ debug/ tests/tooling/        开发、调试及验证工具
├── project-docs/                        工程介绍、移植记录和 Zephyr 学习资料
├── governance/                          Git 协作约定
├── .venv/ .local/                        本机环境，不提交
└── build/                               编译与测试产物，不提交
```

## 构建路径

`scripts/project.py build` 直接调用本仓库 CMake 和 Ninja，以
`uyup_rpi_a/hc32f4a0pitb` 构建 `samples/bringup`。构建显式指定本仓库的 CMSIS_6 与华大 HAL，
不通过外部 west 工作区发现模块。源码快照的版本和文件数保存在
[dependencies.lock.json](../dependencies.lock.json)，解释见 [source-baseline.md](source-baseline.md)。

原始 `west.yml` 保留上游模块目录信息，不表示所有其他厂商 HAL 都已导入。
当前目标只需要已内置的模块；后续功能引入其他模块时，独立记录其来源、版本和许可证。
SDK 与 Python 环境是本机工具，源码工程不将它们纳入版本控制。

课程应用使用独立的 [scripts/learning/run.py](../scripts/learning/README.md)，通过 `--app` 选择实验目录，
按应用、目标与分组记录构建或模拟结果；原有 project.py 继续负责启动示例。
编译对象观察实验另用 inspect_objects.py，生成用于比较符号与布局的文件；它不产生可直接启动的固件。
具体课程入口与当前完成度见[学习路线](learning/README.md)。

## SoC 启动

`soc/xhsc/hc32f4a0` 使用 Zephyr 的 Cortex-M4F 启动路径，声明 144 个外设中断、4 位 NVIC
优先级和 FPU。硬件具有 MPU，但首版未提供区域配置，`CONFIG_ARM_MPU` 保持关闭。

本地 `soc_reset_hook` 在 C 运行时初始化前清除 SRAM 奇偶校验/ECC 状态，并正常返回。
`icg.ld` 在内部 Flash `0x400` 固定保留 24 字的 ICG 配置，使用 KEEP 和链接断言检查位置、
大小与加载偏移；普通代码不得占用该地址。

`soc_early_init_hook` 先使用 MRC 作为低频过渡，配置所有总线 DIV1 与 Flash/SRAM 0 等待，
然后将 PH0/PH1 设为晶振模拟引脚，以适合 12 MHz 的低驱动档启动 XTAL。稳定计数选择最长的
8163 周期档（约 31 ms），软件使用独立的有限轮询预算等待硬件稳定标志，再切换到
**12 MHz XTAL 直驱系统时钟**；PLLH/PLLA 均关闭。稳定失败进入 panic，不以 MRC 静默代替晶振。
8 MHz 过渡和 12 MHz 工作频率均满足 Flash、所有 SRAM 的 0 等待条件。晶振实际起振裕量仍需实板验证。
MRC 规格容差为 ±10%，只用于启动过渡，不作为串口和系统定时器的最终时基。

Zephyr 负责向量表重定位、FPU 与内核初始化。适配只调用 `SystemCoreClockUpdate()`，
不调用会覆盖 VTOR 的厂商 `SystemInit()`。SoC 显式编译所需 DDL 文件，不使用厂商的
reset/vector 回调实现，也不修改厂商源文件。整个编译统一预包含本地 DDL 配置，避免厂商头文件
同目录包含模板而开启未使用的模块或打印重定向。

## 驱动与样例

GPIO 支持基础输入输出；轮询 USART1 使用 PA9/PA10 提供 115200 8N1 控制台。
内核时基使用 Cortex-M SysTick。轮询外设无需 INTC 外设源路由；后续中断驱动需分别配置
HC32 INTC 源选择和 Zephyr/NVIC 中断连接，不能把外设源编号直接当作 NVIC IRQ 号。

`build/bringup` 保存 HC32 镜像；显式 `--board mps2/an386` 使用 `build/mps2`。
`test` 在 QEMU 上执行软件回归，产物位于 `build/twister`。两种目标的镜像与结果分别解释。
板级事实统一在 [hardware.md](hardware.md)，实现与验证进度在 [porting-status.md](porting-status.md)。

## 调试边界

`debug/pyocd.yaml` 使用相对脚本路径，工程入口将仓库根作为 pyOCD `--project`。
目标为 2 MiB Flash 的 `hc32f4a0xi`，板载 DAP 默认 10 MHz SWD，关闭自动解锁擦除。
初始化钩子修正 pyOCD 0.45.1 的主 SRAM 起点为 `0x1FFE0000`，保留 Flash/OTP 算法与全局目标图。

离线检查加载实际配置并核对钩子时序，不打开探针、不访问寄存器。
编译、离线检查、QEMU 与实板验证是不同证据，状态文档分别记录。
