---
id: learning.zephyr-docs.intercore_reference.ipcremainder-191
title: TFM的IPC服务示例
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/samples/tfm_integration/tfm_ipc/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="tfm_ipc"></a>

# 第191章\_TFM的IPC服务示例

原文：[TF-M IPC](https://docs.zephyrproject.org/latest/samples/tfm_integration/tfm_ipc/README.html)。读取日期：2026-10-13，`latest`。

本页翻译 TF-M 可信固件（Trusted Firmware-M）的处理器间通信（Inter-Process Communication，IPC）集成示例，适用于支持 Armv8-M 的开发板。[浏览官方示例源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/tfm_integration/tfm_ipc)。

## 191.1\_工作方式

示例采用 IPC 模式（IPC Mode）：通过 IPC 机制将 TF-M 应用程序编程接口（Application Programming Interface，API）调用送入安全映像（Secure Image）。与之对应的库模式（Library Mode）绕过 IPC，直接调用相应接口。

Zephyr 使用 TF-M 的平台安全架构（Platform Security Architecture，PSA）API，使本示例运行在安全配置下，而 Zephyr 本身运行在非安全配置（Non-secure Configuration）下。示例可作为单线程或多线程（Single-thread/Multi-thread）应用，在控制台（Console）输出测试信息。

应用会在5秒后重启，以演示借助 TF-M 重启。非安全应用不能直接执行重启，因此`sys_reboot()`调用会被转交给 TF-M。

## 191.2\_构建前的目录与命令约定

原页说明项目向控制台输出测试状态和信息，可在 MPS2+ AN521、ST Nucleo L552ZE Q 上构建运行，后面还逐项给出其他平台操作。

阅读说明：下面的原始命令在 Bash 终端中执行，Windows 采用 UCRT64 Bash，Linux 使用 Bash。`$`和`J-Link>`是原页提示符，复制执行时不要把提示符当作命令。`ZEPHYR_ROOT`是 Zephyr 源码根目录：原文的`$ZEPHYR_ROOT`要求已设置此环境变量，`<ZEPHYR_ROOT>`则是需要替换的占位符。

路径以`samples/`开头的 west 示例从 Zephyr 源码根目录执行，以`zephyr/samples/`开头的示例从包含`zephyr`目录的工作区根目录执行；构建完成后的相对文件路径以产生对应`build`目录的位置为基准。原始命令、目标名称和历史版本记录保留，不代表已在当前硬件上复测。以下平台是分别选择的构建路径，不是全部依次执行。

## 191.3\_MPS2+ AN521

采用非安全配置`-DBOARD=mps2/an521/cpu0/ns`构建 Zephyr：

```bash
cd $ZEPHYR_ROOT/samples/tfm_integration/tfm_ipc/
mkdir build
cd build
cmake -DBOARD=mps2/an521/cpu0/ns ..
make
```

也可在包含`zephyr`目录的工作区根目录使用 west：

```bash
$ west build -p -b mps2/an521/cpu0/ns zephyr/samples/tfm_integration/tfm_ipc
```

构建生成应用二进制`mcuboot.bin`和`tfm_sign.bin`后，将它们复制到开发板挂载目录`<MPS2 device name>/SOFTWARE/`。打开板上已有的`<MPS2 device name>/MB/HBI0263C/AN521/images.txt`，按下方原例修改`AN521/images.txt`。其中`TITLE`是标题（Title），`IMAGES`是映像（Images）区段，`TOTALIMAGES`是映像总数；`IMAGE0ADDRESS`／`IMAGE1ADDRESS`分别是两个映像的加载地址（Load Address），`IMAGE0FILE`／`IMAGE1FILE`是映像文件（Image File）。BL2 指第二阶段引导加载器（Second-stage Bootloader）：

```text
TITLE: Versatile Express Images Configuration File

[IMAGES]
TOTALIMAGES: 2 ;Number of Images (Max: 32)

IMAGE0ADDRESS: 0x10000000
IMAGE0FILE: \SOFTWARE\mcuboot.bin  ; BL2 bootloader

IMAGE1ADDRESS: 0x10080000
IMAGE1FILE: \SOFTWARE\tfm_sign.bin ; TF-M with application binary blob
```

配置中文件标题为“Versatile Express 映像配置文件”；共加载两个映像，原注释注明最多32个。第一项是 BL2 第二阶段引导加载器（Second-stage Bootloader），第二项是包含应用二进制块（Application Binary Blob）的 TF-M。两个地址和板内`\SOFTWARE\`路径按原文保留。保存后复位 MPS2+ 开发板。

如果运行 CMake 时遇到下面的错误：

```text
CMake Error at cmake/Common/FindGNUARM.cmake:121 (message):
arm-none-eabi-gcc can not be found.  Either put arm-none-eabi-gcc on the
PATH or set GNUARM_PATH properly.
```

含义是找不到`arm-none-eabi-gcc`，需要将它加入可执行文件搜索路径`PATH`，或正确设置`GNUARM_PATH`。可能需要编辑`tfm_ipc`工程目录下已有的`CMakeLists.txt`，更新原例`-DGNUARM_PATH=/opt/toolchain/arm-none-eabi`中的工具链位置。该路径是原文 Linux 示例，应对应实际安装目录。

## 191.4\_QEMU 模拟运行

MPS2+ AN521 目标`mps2/an521/cpu0/ns`采用双核 Arm Cortex-M33。没有支持的 Armv8-M 开发板时，也可以用 QEMU 模拟器运行 TF-M 测试。

前述正常构建过程也会生成可由`qemu-system-arm`加载的映像。回到包含对应`build`目录的位置执行：

```bash
qemu-system-arm -M mps2-an521 -device loader,file=build/zephyr/tfm_merged.hex -serial stdio
```

也可以在 west 构建命令末尾加`-t run`；使用 Ninja 或 Make 时调用其`run`目标（Target）：

```bash
$ west build -b mps2/an521/cpu0/ns zephyr/samples/tfm_integration/tfm_ipc -t run
```

或者构建完成后，在构建目录执行：

```bash
$ ninja run
```

## 191.5\_ST Nucleo L552ZE Q 与 STM32L562E-DK Discovery

原页记录本示例曾在 Ubuntu 18.04、Zephyr 软件开发套件（Software Development Kit，SDK）0.11.3 上测试。采用非安全配置构建：以下分别是 Nucleo L552ZE Q 与 STM32L562E-DK Discovery 的示例，从 Zephyr 源码根目录执行。

```bash
$ west build -b nucleo_l552ze_q/stm32l552xx/ns samples/tfm_integration/tfm_ipc/
```

```bash
$ west build -b stm32l562e_dk/stm32l562xx/ns samples/tfm_integration/tfm_ipc/
```

构建后，`build/tfm`中会提供设备初始化脚本。`regression.sh`用于设置平台选项字节（Option Bytes）配置并擦除平台。按原顺序烧录：

```bash
$ ./build/tfm/api_ns/regression.sh
$ west flash
```

必须能够通过`PATH`找到`arm-none-eabi-gcc`，而执行`regression.sh`还需要 [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) 提供的`STM32_Programmer_CLI`。脚本运行仍有问题时，返回检查 [Nucleo L552ZE Q](https://docs.zephyrproject.org/latest/boards/st/nucleo_l552ze_q/doc/nucleol552ze_q.html#nucleo_l552ze_q) 或 [STM32L562E-DK Discovery](https://docs.zephyrproject.org/latest/boards/st/stm32l562e_dk/doc/index.html#stm32l562e_dk) 文档的编程与调试（Programming and Debugging）部分。

## 191.6\_LPCxpresso55S69

从 Zephyr 源码根目录使用非安全配置构建：

```bash
$ west build -p -b lpcxpresso55s69_ns samples/tfm_integration/tfm_ipc/ --
```

确保开发板已配置为 [LPC-Link2 J-Link 板载调试探针（Onboard Debug Probe）](../debugging/P003_调试探针.md)，因为这不是开发板出厂时使用的调试接口。

构建得到`tfm_merged.bin`后，从包含对应`build`目录的位置启动 J-Link，再在 J-Link 命令行中依次输入后续命令：

```text
JLinkExe -device lpc55s69 -if swd -speed 2000 -autoconnect 1
J-Link>r
J-Link>erase
J-Link>loadfile build/zephyr/tfm_merged.bin
```

复位并擦除开发板会解除锁定，适用于开发板处于未知状态、无法烧录的情况。烧录映像后还需要手动复位，才能运行代码。

译注：这里保留原页目标名`lpcxpresso55s69_ns`和末尾`--`，没有擅自替换为其他板目标。

## 191.7\_nRF5340 与 nRF9160

使用非安全配置`-DBOARD=nrf5340dk/nrf5340/cpuapp/ns`或`-DBOARD=nrf9160dk/nrf9160/ns`。下面是 nRF9160 的 CMake 与 Ninja 示例；先替换源码路径占位符，删除操作针对当前示例目录下已有的`build`构建产物。

```bash
cd <ZEPHYR_ROOT>/samples/tfm_integration/tfm_ipc/
rm -rf build
mkdir build && cd build
cmake -GNinja -DBOARD=nrf9160dk/nrf9160/ns ..
```

若启用了 BL2，即 MCUboot 引导加载器（Bootloader），需要手动烧录 MCUboot 的`bl2.hex`。下面是 nRF9160 的 Nordic 命令行烧录工具`nrfjprog`原例，其中`NRF91`选择 nRF91 器件系列，在包含对应`tfm/bin/bl2.hex`的构建目录执行：

```bash
nrfjprog -f NRF91 --program tfm/bin/bl2.hex --sectorerase
```

最后烧录拼接后的 TF-M 与 Zephyr 二进制：

```bash
west flash
```

译注：上方原文命令只展示了 CMake 配置，没有列出 Ninja 的实际构建命令。烧录前应先完成所用构建系统的构建，确认相应映像已经生成；这不是已执行或已验证的烧录记录。

## 191.8\_BL5340

使用非安全配置`-DBOARD=bl5340_dvk/nrf5340/cpuapp/ns`。CMake 与 Ninja 原例同样从该示例目录开始，重建`build`目录：

```bash
cd <ZEPHYR_ROOT>/samples/tfm_integration/tfm_ipc/
rm -rf build
mkdir build && cd build
cmake -GNinja -DBOARD=bl5340_dvk/nrf5340/cpuapp/ns ..
```

完成构建后，烧录拼接后的 TF-M 与 Zephyr 二进制；下方相对路径以构建目录为起点：

```bash
west flash --hex-file zephyr/tfm_merged.hex
```

原文也只列出配置与烧录命令；与上一平台一样，烧录前须确认构建已经生成`zephyr/tfm_merged.hex`。

## 191.9\_FRDM-MCXN947

从 Zephyr 源码根目录使用非安全配置构建：

```bash
$ west build -p -b frdm_mcxn947/mcxn947/cpu0/ns samples/tfm_integration/tfm_ipc/
```

确保开发板已使用 LPC-Link2 J-Link 板载调试探针，而不是出厂默认调试接口。构建完成后，通过 J-Link 手动烧录生成的`tfm_merged.bin`：

```text
JLinkExe -device MCXN947_M33_0 -if swd -speed 4000 -autoconnect 1
J-Link>r
J-Link>erase
J-Link>loadfile build/zephyr/tfm_merged.bin
```

复位后执行整片擦除（Full Device Erase），可解除设备锁定并返回已知状态，特别适用于设备处于未知或受保护状态、无法编程的情况。映像成功烧录后，手动复位，开始执行新固件。

## 191.10\_示例输出

以下为官方原始输出，保留其中 TF-M v2.0.0、Zephyr v3.6.0、地址偏移和版本数值。日志的`INF`为信息（Information），`WRN`为警告（Warning），OS 为操作系统（Operating System）；ITS 为内部可信存储（Internal Trusted Storage），PS 为受保护存储（Protected Storage）。`TFM_DUMMY_PROVISIONING`指虚拟预配置（Dummy Provisioning），原输出明确警告它不适合生产：

```text
[INF] Starting bootloader
[INF] Beginning BL2 provisioning
[WRN] TFM_DUMMY_PROVISIONING is not suitable for production! This device is NOT SECURE
[INF] Image index: 1, Swap type: none
[INF] Image index: 0, Swap type: none
[INF] Bootloader chainload address offset: 0x80000
[INF] Jumping to the first image slot
[INF] Beginning TF-M provisioning
[WRN] TFM_DUMMY_PROVISIONING is not suitable for production! This device is NOT SECURE
[WRN] This device was provisioned with dummy keys. This device is NOT SECURE
[Sec Thread] Secure image initializing!
Booting TF-M v2.0.0
Creating an empty ITS flash layout.
Creating an empty PS flash layout.
[INF][Crypto] Provisioning entropy seed... complete.
Timer with period zero, disabling
*** Booting Zephyr OS build v3.6.0 ***
TF-M IPC on (.*)
The version of the PSA Framework API is 257.
The PSA Crypto service minor version is 1.
Generating 256 bytes of random data:
[...]
```

输出依次报告：启动引导加载器、开始 BL2 预配置（Provisioning）、两个映像的交换类型为`none`、链式加载地址偏移为`0x80000`、跳到第一个映像槽位（Image Slot），再开始 TF-M 预配置与安全映像初始化。

其中两次关于`TFM_DUMMY_PROVISIONING`的警告表示：**虚拟预配置不适用于生产，设备不安全**；另一条警告说明设备使用虚拟密钥（Dummy Keys）完成预配置，同样不安全。这些是原输出的安全声明，不能省略。

随后创建空的内部可信存储（Internal Trusted Storage，ITS）和受保护存储（Protected Storage，PS）闪存布局，完成加密服务（Crypto Service）熵种子（Entropy Seed）预配置。周期为0的定时器被禁用。Zephyr 启动后输出 TF-M IPC 平台信息、PSA 框架 API 版本257、PSA 加密服务次版本1，并生成256字节随机数据；`[...]`是原文省略标记，`(.*)`按原文保留。

---

[上一章：IEEE802154的RPMsg示例](P190_IEEE802154的RPMsg示例.md) · [下一章：RPMsg文件系统完整头文件](P192_RPMsg文件系统完整头文件.md) · [返回大纲](大纲.md)
