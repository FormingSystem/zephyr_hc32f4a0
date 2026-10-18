---
id: learning.zephyr-docs.boards-arm.page-3
title: Arm Corstone-1000-A320 Fixed Virtual Platform
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/arm/fvp_corstone1000/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="fvp_corstone1000"></a>

# 第3章\_Arm Corstone-1000-A320固定虚拟平台（FVP）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/arm/fvp_corstone1000/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

开发板概览（Board Overview）

名称（Name）：

`fvp_corstone1000`

厂商（Vendor）：

[Arm公司（ARM Ltd.）](https://docs.zephyrproject.org/latest/boards/index.html#vendor=arm)

状态（Status）：

当前未积极维护（Not Actively Maintained）

架构（Architecture）：

[arm64](https://docs.zephyrproject.org/latest/boards/index.html#arch=arm64)

片上系统（SoC）：

[a320](https://docs.zephyrproject.org/latest/boards/index.html#soc=a320)

<a id="board-github-link"></a>

[浏览开发板源码（Browse Board Sources）](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/arm/fvp_corstone1000/doc/index.rst/../..)<a id="arm-corstone-1000-a320-fixed-virtual-platform"></a>

## Arm Corstone-1000-A320固定虚拟平台（FVP）

<a id="overview"></a>

### 概述（Overview）

此开发板配置使用Arm Corstone-1000-A320固定虚拟平台（FVP），模拟以Cortex-A320为主处理器的Arm Corstone-1000参考设计。

Corstone-1000是面向安全物联网（Secure IoT）系统的Arm参考设计，具有：


- 使用Cortex-A320（ARMv9.2-A）的主处理器子系统（Host Processor Subsystem）
- 运行可信固件M（TF-M）的安全隔离区（Secure Enclave，Cortex-M0+）
- Ethos-U85神经网络处理单元（NPU / Neural Processing Unit）
- CryptoCell-312硬件加速器
- 通过MCUboot验证启动（Verified Boot）实现系统级安全

此配置支持：


- Cortex-A320 CPU，ARMv9.2-A架构
- 通用中断控制器v3（GICv3），GIC-600
- ARM架构通用定时器（Architected Generic Timer）
- PL011 UART控制器
- 可伸缩向量扩展2（SVE2 / Scalable Vector Extension 2）

注意（Note）

FVP模型包含Ethos-U85 NPU，但当前开发板配置尚不支持它。

<a id="hardware"></a>

### 硬件（Hardware）

<a id="supported-features"></a>

#### 支持的功能（Supported Features）

`fvp_corstone1000`开发板支持下表所列的硬件功能。

片上／板载（On-Chip / On-Board）

功能集成在片上系统（SoC）内／位于开发板上。

2 / 2

分别表示已启用／已禁用的实例数。点击数量标签，可查看开发板或SoC设备树源码（DTS）中该功能的第一个实例。

`vnd,foo`

与此功能匹配的设备树绑定兼容字符串（Compatible String）；点击链接可查看绑定文档。

<a id="fvp_corstone1000-hw-features"></a>

<a id="fvp_corstone1000-fvp_corstone1000/a320-hw-features-section"></a>

##### `fvp_corstone1000/a320`目标（Target）

<a id="fvp_corstone1000-fvp_corstone1000/a320-hw-features-panel"></a>

<a id="fvp_corstone1000-fvp_corstone1000/a320-hw-features-memory"></a>

该开发板目标的片上存储容量：128 MiB RAM、N/A Flash。

<a id="fvp_corstone1000-fvp_corstone1000/a320-hw-features-table"></a>

<table>
<tr>
<th>类型（Type）</th>
<th>位置（Location）</th>
<th>说明（Description）</th>
<th>兼容字符串（Compatible）</th>
</tr>
<tr>
<td rowspan="1">中央处理器（CPU）</td>
<td>板载（On-Board）</td>
<td>Arm Cortex-A320处理器（CPU）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_corstone1000/fvp_corstone1000.dtsi?plain=1#L29">已启用：4</a>）</td>
<td><a href="../cpu_arm_riscv_binding_reference/P006_arm_cortex-a320.md#std-dtcompatible-arm-cortex-a320"><code>arm,cortex-a320</code></a></td>
</tr>
<tr>
<td rowspan="1">时钟控制（Clock Control）</td>
<td>板载（On-Board）</td>
<td>通用固定频率时钟提供者（Fixed-Rate Clock Provider）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_corstone1000/fvp_corstone1000.dtsi?plain=1#L63">已启用：1</a>）</td>
<td><a href="../hardware/P566_固定时钟绑定.md#dtbinding-fixed-clock"><code>fixed-clock</code></a></td>
</tr>
<tr>
<td rowspan="1">中断控制器（Interrupt Controller）</td>
<td>板载（On-Board）</td>
<td>ARM通用中断控制器（GIC）v3（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_corstone1000/fvp_corstone1000.dtsi?plain=1#L72">已启用：1</a>）</td>
<td><a href="../interrupt_fabric_binding_reference/P004_arm_gic-v3.md#std-dtcompatible-arm-gic-v3"><code>arm,gic-v3</code></a></td>
</tr>
<tr>
<td rowspan="1">电源管理 CPU 操作（Power Management CPU Operations）</td>
<td>板载（On-Board）</td>
<td>电源状态协调接口（PSCI / Power State Coordination Interface）0.2版（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_corstone1000/fvp_corstone1000.dtsi?plain=1#L13">已启用：1</a>）</td>
<td><a href="https://docs.zephyrproject.org/latest/build/dts/api/bindings/pm_cpu_ops/arm%2Cpsci-0.2.html#std-dtcompatible-arm-psci-0.2"><code>arm,psci-0.2</code></a></td>
</tr>
<tr>
<td rowspan="1">串行控制器（Serial Controller）</td>
<td>板载（On-Board）</td>
<td>ARM PL011通用异步收发器（UART）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_corstone1000/fvp_corstone1000.dtsi?plain=1#L83">已启用：1</a>）</td>
<td><a href="../uart_adi_arm_atmel_binding_reference/P008_arm_pl011.md#std-dtcompatible-arm-pl011"><code>arm,pl011</code></a></td>
</tr>
<tr>
<td rowspan="1">定时器（Timer）</td>
<td>板载（On-Board）</td>
<td>每个内核独立的ARM架构定时器（Architected Timer）（<a href="https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/fvp_corstone1000/fvp_corstone1000.dtsi?plain=1#L50">已启用：1</a>）</td>
<td><a href="../arm_interrupt_timer_binding_reference/P010_ARMv8架构定时器.md#std-dtcompatible-arm-armv8-timer"><code>arm,armv8-timer</code></a></td>
</tr>
</table>

<a id="board-variants"></a>

#### 开发板变体（Board Variants）

可使用以下开发板目标：


- `fvp_corstone1000/a320`：单核ARMv9.2-A，Cortex-A320 CPU
- `fvp_corstone1000/a320/smp`：四核对称多处理（SMP），使用全部四个Cortex-A320 CPU

<a id="memory-map"></a>

#### 内存映射（Memory Map）

Corstone-1000-A320 FVP主处理器子系统的内存布局如下：

<table>
<tr>
<th>区域（Region）</th>
<th>地址（Address）</th>
<th>大小（Size）</th>
</tr>
<tr>
<td>动态随机存取存储器（DRAM）</td>
<td>0x80000000</td>
<td>2 GB</td>
</tr>
<tr>
<td>GIC分发器（Distributor）</td>
<td>0x1C000000</td>
<td>64 KB</td>
</tr>
<tr>
<td>GIC再分发器（Redistributor）</td>
<td>0x1C040000</td>
<td>2 MB</td>
</tr>
<tr>
<td>主处理器UART0（Host UART0）</td>
<td>0x1A510000</td>
<td>4 KB</td>
</tr>
</table>

<a id="boot-architecture"></a>

### 启动架构（Boot Architecture）

Corstone-1000使用涉及两个处理器的多阶段启动流程：

```text
Secure Enclave (M0+):  BL1_1 -> BL1_2 -> BL2/MCUboot -> TF-M SPE -.
                                                                     |
Host CPU (A320):                                TF-A BL2 -> BL31 -> Zephyr (BL33)
```

安全隔离区（Secure Enclave，Cortex-M0+）：


1. BL1_1（ROM）：硬件初始化及密钥配置（Key Provisioning）
2. BL1_2（一次性可编程存储器，OTP）：由BL1_1验证
3. BL2（MCUboot）：解析GUID分区表（GPT），加载TF-M与TF-A镜像，并使用椭圆曲线数字签名算法（ECDSA）验证
4. TF-M运行时（Runtime）：初始化内部可信存储／受保护存储／密码服务分区（ITS/PS/Crypto），通过DSU-120T电源策略单元（PPU）给主CPU上电

主CPU（Host CPU，Cortex-A320）：


1. TF-A BL2：由MCUboot加载，解析固件镜像包（FIP），加载BL31和BL33
2. TF-A BL31：异常级别3（EL3）运行时，提供电源状态协调接口（PSCI）及GIC初始化，通过异常返回（ERET）进入非安全EL1（NS-EL1）
3. BL33（Zephyr）：运行于EL1的非安全应用

注意（Note）

FVP的配置周期在真正启动前需要完整执行两轮安全隔离区（SE）启动，这是正常现象：第一轮会配置占位密钥（Dummy Keys）并重启。

<a id="programming-and-debugging"></a>

### 烧录与调试（Programming and Debugging）

<a id="prerequisites"></a>

#### 前置条件（Prerequisites）


1. [Zephyr SDK](../toolchains/P002_ZephyrSDK.md#toolchain-zephyr-sdk)（推荐）：提供供TF-M使用的`arm-zephyr-eabi`、供Zephyr／TF-A构建使用的`aarch64-zephyr-elf`，以及供TF-A设备树编译使用的`dtc`。
2. Corstone-1000-A320 FVP：从[Arm Ecosystem FVPs](https://developer.arm.com/Tools%20and%20Software/Fixed%20Virtual%20Platforms/IoT%20FVPs)下载。

  将环境变量`ARMFVP_BIN_PATH`设为FVP二进制程序所在目录，默认安装路径示例如下：

  ```text
  export ARMFVP_BIN_PATH=~/FVP_Corstone_1000-A320/models/Linux64_GCC-9.3
  ```
3. `sgdisk`：创建GPT分区表所需，可通过`gdisk`软件包安装：

  ```text
  # Fedora / RHEL
  sudo dnf install gdisk

  # Ubuntu / Debian
  sudo apt install gdisk
  ```

<a id="building"></a>

#### 构建（Building）

此开发板需要支持Corstone-1000-A320的TF-M和TF-A模块。检出此分支后更新模块：

```text
west update
```

此开发板需要[系统构建（Sysbuild / System Build）](../sysbuild/P001_系统构建.md#sysbuild)，在构建Zephyr时自动构建TF-M（安全隔离区）和TF-A（主处理器固件）：

```text
west build -b fvp_corstone1000/a320 samples/hello_world --sysbuild
```

尖端触点（Tip）

若不想每次都传入`--sysbuild`，可将其设为默认值：

```text
west config build.sysbuild true
```

将在`build/firmware/`中生成：


- `bl1.bin`：安全隔离区ROM镜像，包含BL1_1及配置包（Provisioning Bundle）
- `cs1000.bin`：32 MB GPT闪存镜像，其中FIP包含已签名的TF-M、已签名的TF-A BL2、BL31及Zephyr

<a id="running"></a>

#### 运行（Running）

```text
west build -t run
```

若要设置模拟时间限制或其他FVP选项，在配置阶段设置`ARMFVP_EXTRA_FLAGS`：

```text
ARMFVP_EXTRA_FLAGS="--simlimit 120" west build -b fvp_corstone1000/a320 \
    samples/hello_world --sysbuild
west build -t run
```

预期输出（配置周期结束后）：

```text
*** Booting Zephyr OS build v4.3.0-... ***
Hello World! fvp_corstone1000/a320
```

<a id="debugging"></a>

#### 调试（Debugging）

详细概述见[应用调试（Application Debugging）](https://docs.zephyrproject.org/latest/develop/debug/index.html#application-debugging)。

FVP支持通过Arm Development Studio或其他使用Iris调试接口的调试器连接。

尖端触点（Tip）

在UART尚不可用的早期启动阶段，可启用[`CONFIG_SEMIHOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SEMIHOST)及[`CONFIG_SEMIHOST_CONSOLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SEMIHOST_CONSOLE)、禁用[`CONFIG_UART_CONSOLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_CONSOLE)，使用半主机机制（Semihosting）调试。FVP默认启用半主机支持。

<a id="known-limitations"></a>

#### 已知限制（Known Limitations）


- 仅支持Linux／Unix主机：Sysbuild集成使用POSIX shell工具（`sh`、`dd`、`sgdisk`）组装安全隔离区闪存镜像，当前不支持Windows主机。
- Ethos-U85 NPU：FVP模型中包含此NPU，但Zephyr当前尚不支持。
- 内存映射重叠警告（mmap overlap warning）：TF-A BL2／BL31会出现`mmap_add_region_check() failed. error -22`。这是发布模式（Release Mode）下Ethos-U85内存映射重叠引起的非致命警告，Yocto参考构建也会出现。

<a id="references"></a>

### 参考资料（References）


- [Arm Corstone-1000技术概述（Technical Overview）](https://developer.arm.com/documentation/102360/latest/)
- [Arm Cortex-A320](https://developer.arm.com/Processors/Cortex-A320)
- [Corstone-1000软件文档（Software Documentation）](https://corstone1000.docs.arm.com/en/corstone1000-2025.12/index.html)
- [Corstone-1000 Armv9-A边缘人工智能生态固定虚拟平台（Edge-AI Ecosystem FVP）](https://developer.arm.com/Tools%20and%20Software/Fixed%20Virtual%20Platforms/IoT%20FVPs)

## 译注

本页原文明确要求使用支持Corstone-1000-A320的TF-M／TF-A模块及Sysbuild，且该Sysbuild集成目前只支持Linux／Unix主机。Ethos-U85存在于模型中不代表Zephyr已支持；TF-A内存映射重叠警告的非致命说明也按原文保留。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [Cortex-A320](https://developer.arm.com/Processors/Cortex-A320)：<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)>。
- [IoT%20FVPs](https://developer.arm.com/Tools%20and%20Software/Fixed%20Virtual%20Platforms/IoT%20FVPs)：<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)>。
- [](https://developer.arm.com/documentation/102360/latest/)：<urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)>。

---

[上一章](P002_FVP_BaseR_AEMv8-R.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P004_ARM_Ltd..md)
