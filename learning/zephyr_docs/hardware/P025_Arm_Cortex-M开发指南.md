---
id: learning.zephyr-docs.hardware.cortex-m
title: Arm_Cortex-M开发指南
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/hardware/arch/arm_cortex_m.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第25章\_Arm Cortex-M开发指南

原文：[Arm Cortex-M Developer Guide](https://docs.zephyrproject.org/latest/hardware/arch/arm_cortex_m.html)。读取日期：2026-10-12，`latest`。

本页说明 Zephyr **实时操作系统（Real-Time Operating System，RTOS）** 的 Arm Cortex-M 架构移植状态，以及在 Cortex-M 平台开发应用时需要了解的关键机制。

## 25.1\_主要功能支持

下表按原文列出各处理器实现的支持状态，Y 为支持，N 为不支持。架构分组为：M0/M1/M0+ 属于 Arm v6-M；M3/M4/M7 属于 Arm v7-M；M23/M33 属于 Arm v8-M；M55/M85 属于 Arm v8.1-M。

| 功能 | M0/M1 | M0+ | M3 | M4 | M7 | M23 | M33 | M55 | M85 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 可编程故障异常优先级 | N | N | Y | Y | Y | N | Y | Y | Y |
| 单线程内核 | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| 线程局部存储 | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| 常规中断 | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| 动态中断 | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| 直接中断 | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| 零延迟中断 | N | N | Y | Y | Y | Y | Y | Y | Y |
| **中央处理器（Central Processing Unit，CPU）** 空闲 | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| 原生系统定时器 SysTick | N [1] | Y | Y | Y | Y | Y | Y | Y | Y |
| 用户模式 | N | Y | Y | Y | Y | Y | Y | Y | Y |
| **内存保护单元（Memory Protection Unit，MPU）** 硬件栈保护 | N | N | Y | Y | Y | Y | Y | Y | Y |
| 硬件栈界限检查 | N | N | N | N | N | Y [2] | Y | Y | Y |
| 特权禁止执行 PXN [3] | N | N | N | N | N | N | N | Y | Y |
| PACBTI 硬件控制流完整性 | N | N | N | N | N | N | N | N | Y |
| 硬件辅助空指针解引用检测 | N | N | Y | Y | Y | Y | Y | Y | Y |
| 硬件辅助原子操作 | N | N | Y | Y | Y | N | Y | Y | Y |
| 不缓存区域 | N | N | Y | Y | Y | N | Y | Y | Y |
| 在 SRAM 执行函数 | N | N | Y | Y | Y | N | Y | Y | Y |
| 浮点服务 | N | N | N | Y | Y | N | Y | Y | Y |
| DSP 指令集 | N | N | N | Y | Y | N | Y | Y | Y |
| 原生 TrustZone-M | N | N | N | N | N | Y | Y | Y | Y |
| TF-M 集成 | N | N | N | N | N | N | Y | N | N |
| 代码重定位 | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| 软件向量表转发 | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| 硬件辅助计时函数 | N | N | Y | Y | Y | N | Y | Y | Y |

原文脚注：[1] Cortex-M1 的 SysTick 是可选功能；[2] Cortex-M23 仅安全构建支持栈界限检查；[3] PXN 见 [Arm 特权禁止执行说明](https://developer.arm.com/documentation/107655/100/RTOS-and-Secure-software-design-considerations/Secure-software-development-design-considerations/Security-and-privilege-combination/Using-PXN-bit?lang=en)。

> 译注：这是所读取文档的 Zephyr 支持矩阵，不是每款 **片上系统（System on Chip，SoC）** 的硬件保证。表中某些合并项也过于粗略，例如 M0/M1 的 SysTick 一栏，以及 M23 零延迟项与后文 Mainline/BASEPRI 机制之间的适用关系；实际能力需核对目标硬件和构建选项。不能仅凭 Y 就认定指定芯片配备了可选 FPU、MPU 或对应平台集成。

## 25.2\_线程与栈

每线程有自己的栈，架构还管理异常所用中断栈及切换期间的上下文保存。

### 25.2.1\_栈对齐与栈指针

Cortex-M 默认要求线程栈双字对齐，见 `CONFIG_STACK_ALIGN_DOUBLE_WORD`。启用基于 MPU 的栈溢出检测 `CONFIG_MPU_STACK_GUARD` 后，对齐要求更大，由 `CONFIG_ARM_MPU_REGION_MIN_ALIGN_AND_SIZE` 反映。

Arm v6-M / v7-M 若启用 `CONFIG_USERSPACE`，线程栈还必须按自身大小对齐，大小是 2 的幂；此要求由 `CONFIG_MPU_REQUIRES_POWER_OF_TWO_ALIGNMENT` 强制。

线程模式使用进程栈指针 PSP，处理异常和硬件中断的处理程序模式使用主栈指针 MSP。这样切换线程时可以修改 PSP，而不干扰当前异常处理流程。

Cortex-M 中各异常和中断共享中断栈。嵌套中断会增加栈帧，选择 `CONFIG_ISR_STACK_SIZE` 时必须计入嵌套需求。中断栈还用于早期启动，使内核能先建立主线程栈，再切换到主线程。

### 25.2.2\_线程上下文切换

线程切换由 PendSV 异常触发。所有 Cortex-M 实现都有 PendSV，Zephyr 将它设置为最低中断优先级，以利用尾链机制减少切换次数，并避免提高硬件中断延迟。

切换过程不是原子的，可以被硬件中断抢占；但一次线程切换必须结束，才能开始下一次线程切换。

换出时通常保存以下内容：

- 被调用者保存寄存器 R4～R11，存入内核内存中的线程上下文容器。
- 当前运行模式：用户或特权模式、是否存在活动浮点上下文，以及当前 PendSV 的 `EXC_RETURN` 值。
- 有活动浮点上下文时，将被调用者保存浮点寄存器 S16～S31 存入线程浮点上下文容器。
- 当前 PSP，它指向线程异常栈帧起始位置；该帧包含调用者保存上下文与返回地址。

换入时通常恢复普通被调用者保存寄存器、运行模式及需要的浮点寄存器；重编程动态 MPU 区域，使用户线程能访问自己的栈与应用内存，并按配置设置特权栈底部保护区；恢复 PSP，以及 `CONFIG_BUILTIN_STACK_GUARD` 对应栈指针界限寄存器。若启用 `CONFIG_STACK_SENTINEL`，还检查换入线程的栈哨兵。

PendSV 异常返回时，通过异常帧退栈恢复调用者保存寄存器与返回地址。实现位于 `arch/arm/core/cortex_m/swap_helper.S`。

### 25.2.3\_Armv8-M栈界限检查

Armv8-M 和 Armv8.1-M 可用 `MSPLIM`、`PSPLIM` 核心寄存器检查栈界限，通过 `CONFIG_BUILTIN_STACK_GUARD` 启用。

线程的用户栈或特权栈由 PSPLIM 保护，中断栈由 MSPLIM 保护。MSPLIM 启动时设置一次；PSPLIM 在线程切换，或系统调用切换普通栈与特权栈时重新设置。原文个别位置拼作 `PSLIM`，此处统一为寄存器名 `PSPLIM`。

重编程使用 MSR 指令，运行开销小，不影响中断延迟，不占用保护区内存，也不消耗 MPU 区域，因此是一种轻量而高效的检测方式。原文说明溢出触发专用 UsageFault。

> 译注：需结合前表的 Baseline/Secure 限制理解寄存器与异常可用性，不将 Mainline 的完整故障处理机制直接推广到所有 Cortex-M23 构建。

## 25.3\_异常与中断处理

中断优先级、屏蔽方式及直接中断决定内核与外设中断如何交互。

### 25.3.1\_优先级数量

可配置优先级数量取决于嵌套向量中断控制器 NVIC 实现了多少优先级位，平台需在设备树中描述：

```dts
&nvic {
        arm,num-irq-priority-bits = <#priority-bits>;
};
```

> 译注：`#priority-bits` 是原文占位符，实际设备树要替换成该 SoC 实现的位数，不是可原样使用的数值。

### 25.3.2\_内核保留优先级

系统故障异常设计上处于最高优先级。Baseline Cortex-M 只有 HardFault 处理器故障异常，其优先级由硬件固定，高于所有可配置异常。Mainline 的 MemManageFault、UsageFault 等可配置故障异常被设为最高可配置优先级，能力符号是 `CONFIG_CPU_CORTEX_M_HAS_PROGRAMMABLE_FAULT_PRIOS`。

通常硬件中断不与该级别共享，因此普通 **中断服务例程（Interrupt Service Routine，ISR）** 中的处理器故障可由相应异常处理程序处理，而不升级为 HardFault；线程模式同样如此。

SVC 通常也处于最高可配置优先级，用于分派系统调用、触发内核 oops/panic 等运行错误，或实现中断下放。

Baseline 中，SVC 可以与其他异常或硬件中断共享最高可配置级别。因此 ISR 中产生内核运行错误可能升级为 HardFault，故障例程用额外逻辑识别它。Mainline 则保留 SVC 优先级，通常只与可配置处理器故障共享；普通硬件中断优先级更低，所以 ISR 中的内核错误仍可由 SVC 处理，无须升级。

启用 Mainline 零延迟中断 `CONFIG_ZERO_LATENCY_IRQS` 时是例外：零延迟中断取最高可配置优先级，SVC 下移到第二高，常规硬件中断仍低于 SVC。优先级配置位于 `include/zephyr/arch/arm/cortex_m/exception.h`。

### 25.3.3\_中断锁

Baseline 通过 PRIMASK 实现中断锁。原文所示入口为：

```c
arch_irq_lock()
```

该操作把 PRIMASK 设为 1，屏蔽全部可配置优先级中断。这满足内核锁中断要求，但此时通过 SVC 触发的运行错误会升级为 HardFault。

Mainline 选择 `CONFIG_CPU_CORTEX_M_HAS_BASEPRI`，以 BASEPRI 或 BASEPRI_MAX 实现屏蔽。`arch_irq_lock()` 屏蔽系统与硬件中断，但保留 SVC、处理器故障和零延迟中断。

这样零延迟中断可进入内核临界区，处理器和内核故障在锁中断前后采用相同处理路径，系统调用也能在中断被锁时分派。

原文强调 Mainline 默认设计尽量由对应异常处理程序处理错误，把 HardFault 留给安全关键应用的特殊情况，并将“不会升级”描述得很强。

> 译注：不能把这段理解成任何情况下都不可能 HardFault。本页后文即说明零延迟 ISR 内故障会升级；异常自身故障、屏蔽或配置变化也要结合架构规则分析。

### 25.3.4\_动态直接中断

Cortex-M 支持在运行时安装直接 ISR。直接中断绕过部分通用 Zephyr 处理路径，适用于性能敏感场景。

通过 `CONFIG_DYNAMIC_DIRECT_INTERRUPTS` 启用，同时必须启用内核动态中断支持 `CONFIG_DYNAMIC_INTERRUPTS`。

### 25.3.5\_零延迟中断

Mainline 默认把最高可配置级别留给 SVC，不受普通中断锁屏蔽。启用 `CONFIG_ZERO_LATENCY_IRQS` 后，可把零延迟中断放在最高优先级，使其不被内核锁阻塞，并抢占普通硬件或系统中断。

由于其优先级高于内核异常，零延迟 ISR 不能使用任何内核功能。它与处理器故障优先级相同，因此其内部故障会升级为 HardFault，不能按普通处理器故障路径处理。开发者必须了解这一限制。

## 25.4\_CPU空闲

Cortex-M 实现 `k_cpu_idle()` 和 `k_cpu_atomic_idle()`，位于 `arch/arm/core/cortex_m/cpu_idle.c`。两者都尝试进入低功耗状态；前者执行 WFI（等待中断），后者执行 WFE（等待事件）。

原文要求在中断已锁状态调用，由内核空闲线程使用时内核负责这一点；原文还称唤醒后两者都无条件恢复中断，不管调用前锁状态如何。

> 译注：后一句对 `k_cpu_atomic_idle(key)` 过于笼统。本地实现唤醒后执行 `arch_irq_unlock(key)`，恢复传入键对应状态，Mainline 再清除临时 PRIMASK。应按接口合同传入正确中断键，不把原子空闲理解为无条件解除任意嵌套锁。通用用法见[调度与CPU空闲](../kernel/P005_调度与CPU空闲.md)。

## 25.5\_内存保护与系统调用

具有标准 Arm MPU，或提供类似内存访问策略机制的平台，例如 Kinetis 的 NXP MPU，可以支持用户模式。原文说明在开发板默认 Kconfig 中启用 `CONFIG_ARM_MPU` 时，会选择 `CONFIG_ARCH_HAS_USERSPACE`。

### 25.5.1\_用户模式系统调用

线程通过同步 SVC 异常发起系统调用。原文称最多五个参数放入 R1～R5，系统调用 ID 放入 R6。

> 译注：参数段属于旧说明。本地 `include/zephyr/arch/arm/syscall.h` 的 `arch_syscall_invoke6()` 使用 R0～R5 传六个参数、R6 传调用 ID。实际调用约定应以目标版本架构头文件及生成包装函数为准，不按“五个参数”实现新的分派器。

SVC 处理程序进入系统调用准备逻辑：把 PSP 改到线程特权栈，必要时更新 PSPLIM；修改 CONTROL 使线程返回后处于特权模式；修改 SVC 异常帧中的返回地址，使异常返回后在特权线程模式执行系统调用分派代码。

执行完后，分派代码恢复用户原 PSP、PSPLIM 和 CONTROL 非特权模式，再返回调用者。

系统调用本体在线程模式执行，可随时被中断抢占，也可能被调度换出；线程再次换入后继续。原文下一段又称“分派器在 SVC 优先级执行，除零延迟中断外不能被硬件中断抢占”，并指出准备阶段可能增加中断延迟。

> 译注：这两段必须区分 SVC 异常中的准备过程和异常返回后的系统调用本体。前者受 SVC 优先级影响，后者在线程模式执行；不能把整次系统调用当成一直持有 SVC 优先级。

### 25.5.2\_MPU栈溢出检测

有 MPU 的平台可启用 `CONFIG_MPU_STACK_GUARD`。原文强调：触及栈保护区域时产生处理器故障；此机制主要用于监督线程及用户线程处于特权模式时的栈保护；用户模式栈越界由用户访问权限限制检测，不依赖该开关。

原文同时说明，检测监督线程溢出不保证此前没有内存被破坏。通常为栈保护保留一个 MPU 区域；某些启用 `CONFIG_MPU_GAP_FILLING` 的 Arm v8-M 配置需要两个区域。

MPU 保护区在线程切换时重编程，给切换增加少量开销；与内建栈界限检查不同，它不在每次系统调用切栈时重编程。

Arm v8-M 启用 `CONFIG_HW_STACK_PROTECTION` 时，默认采用原生栈界限机制，而不是 MPU 保护；需要时可手动启用 `CONFIG_MPU_STACK_GUARD` 覆盖默认选择。

> 译注：原文将“所有溢出都能检测”表述得过于绝对。有限保护区的检查发生在实际受保护地址访问时，不能把它当作任意跨度越界访问都在首次发生前被拦截的保证；也不能代替栈容量设计。

### 25.5.3\_PACBTI控制流保护

Armv8.1-M 的可选 PACBTI 扩展包含指针认证（Pointer Authentication）与分支目标识别（Branch Target Identification）。PAC-RET 对返回地址签名并认证，缓解返回导向编程攻击；BTI 在合法分支目标放置指令，缓解跳转导向编程攻击。

硬件和编译器支持时，例如 Cortex-M85，可选择以下配置之一：`CONFIG_ARM_PACBTI_STANDARD`、`CONFIG_ARM_PACBTI_PACRET`、`CONFIG_ARM_PACBTI_PACRET_LEAF`、`CONFIG_ARM_PACBTI_BTI`、`CONFIG_ARM_PACBTI_PACRET_BTI`、`CONFIG_ARM_PACBTI_PACRET_LEAF_BTI`、`CONFIG_ARM_PACBTI_NONE`。

所选配置将相应编译器参数加入构建，例如 GCC 的 `-mbranch-protection=`。根据 `CONFIG_ARM_PACBTI` 所选模式，自动选择 `CONFIG_ARM_PAC`、`CONFIG_ARM_BTI`，通过 CONTROL 寄存器及固定虚拟平台（FVP）中的相应位启用能力。

启用 `CONFIG_ARM_PAC_PER_THREAD` 可使用具备密码学安全性的每线程 PAC 密钥；密钥生成源与配置见该选项帮助。

限制是只有带 PACBTI 硬件的 Armv8.1-M Mainline 目标才能完整使用。原文还称集成 **软件开发工具包（Software Development Kit，SDK）** 的 GCC 12.2 不支持 PACBTI，建议外部 GCC 14.3 或更新版本，配置方法见[工具链](../toolchains/大纲.md)。

> 译注：SDK 内含版本这句属于原文快照，不表示本机已安装工具链版本。本次未安装、更换或检测 PACBTI 编译器；选择时应核对实际版本能力。

进一步说明见 [Arm PACBTI 文档](https://developer.arm.com/documentation/109576/latest/)与 [Arm 技术文章](https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/armv8-1-m-pointer-authentication-and-branch-target-identification-extension)。

## 25.6\_内存映射与MPU区域

MPU 区域分为固定、附加静态和按线程动态设置三类，总数量由硬件限制。

### 25.6.1\_固定区域

启用 `CONFIG_ARM_MPU` 时，启动阶段默认设置：

- 整个 Flash 为可读、可执行。`CONFIG_MPU_ALLOW_FLASH_WRITE` 可改为可读写执行；启用 `CONFIG_USERSPACE` 时允许非特权访问整个 Flash 区域。
- 整个 SRAM 为仅特权可读写、不可执行。Arm v8-M 关闭 `CONFIG_MPU_GAP_FILLING` 时例外：不建立整个 SRAM 区域，使用 Arm 默认背景映射，允许特权读写执行。
- 设备树 `zephyr,memory-attr` 描述的内存区域，按相应 MPU 属性设置。

这些默认区域定义在 `arch/arm/core/mpu/arm_mpu_regions.c`。启用 `CONFIG_CPU_HAS_CUSTOM_FIXED_SOC_MPU_REGIONS` 表示 SoC 自行定义并配置固定 MPU 区域，以替代默认布局。

### 25.6.2\_设备树定义固定区域

内存节点有 `zephyr,memory-attr` 时，启动阶段会分配并设置相应 MPU 区域。配合 [`zephyr,memory-region`](https://docs.zephyrproject.org/latest/build/dts/api/bindings/base/zephyr%2Cmemory-region.html) 兼容属性，还会生成与之关联的链接段。

以下例子定义不缓存内存区域：

```dts
sram_no_cache: memory@20300000 {
     compatible = "zephyr,memory-region", "mmio-sram";
     reg = <0x20300000 0x100000>;
     zephyr,memory-region = "SRAM_NO_CACHE";
     zephyr,memory-attr = <DT_MEM_ARM_MPU_RAM_NOCACHE>;
};
```

这会根据设备树中的名称、基地址、大小及属性建立 MPU 条目。细节见[缓存基础](P021_缓存基础.md)和[内存属性](https://docs.zephyrproject.org/latest/services/mem_mgmt/index.html)。

> 译注：`0x20300000` 与容量是原文示例，不能直接作为 HC32 内存地址使用；实际芯片、总线可达性、MPU 对齐及链接区域均需匹配。

### 25.6.3\_附加静态区域

为以下功能，启动时还可能设置额外区域：

- 启用 `CONFIG_ARCH_HAS_RAMFUNC_SUPPORT` 且用户定义 SRAM 执行函数时，用可读执行区域承载这些函数。
- 启用 `CONFIG_CODE_DATA_RELOCATION_SRAM` 时，为移到 SRAM 的代码建立可读执行区域。
- 启用 `CONFIG_NOCACHE_MEMORY` 时，建立不缓存 SRAM 区域。
- 启用 `CONFIG_COVERAGE_GCOV` 时，为 GCOV 覆盖率计数区域建立可读写、必要时非特权可访问的区域。
- 启用 `CONFIG_NULL_POINTER_EXCEPTION_DETECTION_MPU` 时，用禁止访问区域检测空指针解引用。

静态区域边界来自链接器暴露的符号，原文路径写为 `include/linker/linker-defs.h`。

### 25.6.4\_动态区域

每次线程切换可能重编程以下线程相关区域：用户线程栈的非特权可读写区域；只读的 MPU 栈保护区域；当前线程应用内存域分区的非特权可读写区域。

### 25.6.5\_区域预算和空隙填充

MPU 区域数有限。原文说明多数平台有 8 个，一些 Cortex-M33 或 M7 平台可能有 16 个。固定、静态与动态区域必须共同满足此上限，8 区域平台未必能同时启用全部功能；实际应用通常只需其中一部分，因此也常常够用。

Arm v8-M MPU 不允许区域重叠。`CONFIG_MPU_GAP_FILLING` 控制是否设置覆盖整个 SRAM 的固定区域。启用时，为插入静态、动态区域必须对完整 SRAM 做分割，增加所需区域数；关闭时，不设置整体 SRAM 区域，静态和动态区域叠加在始终存在的背景映射策略上，不必完整切分。

但背景 SRAM 允许执行代码，因此关闭该配置时，不再通过该机制防止从 SRAM 执行恶意代码。

## 25.7\_浮点服务

Cortex-M 支持浮点寄存器非共享与共享两种模式，详见[浮点服务](../kernel/P032_浮点服务.md)。

启用 `CONFIG_FPU` 时，默认启用 `CONFIG_FPU_SHARING`。原因是某些编译器配置即使没有显式浮点计算，也可能为任意线程生成浮点指令、激活浮点上下文，切换时必须保存它。

只有能保证镜像中除了一个获准线程之外绝不产生浮点指令时，才能关闭共享，采用非共享模式。

共享模式下，有活动浮点上下文的线程在换出、换入时保存和恢复被调用者保存浮点寄存器，增加运行开销；每线程还需额外内存保存这些寄存器，并预留异常入口保存调用者浮点寄存器所需栈空间。

延迟压栈默认启用，原文说明常规中断不会立即承担浮点压栈开销，浮点上下文实际保存主要在 PendSV 切换路径触发。

> 译注：上述延迟压栈说明不能理解为 ISR 任意使用浮点仍无额外开销；使用范围和栈预算还需遵循浮点服务章节。

## 25.8\_镜像启动、链接和CMSIS

Cortex-M 应用既可独立启动，也可由引导程序或其他应用链式加载。后者通常放在 Flash 中指定代码分区；`CONFIG_USE_DT_CODE_PARTITION` 让镜像链接到设备树所指定分区。

### 25.8.1\_启动硬件初始化

链式加载镜像可能要求核心寄存器和外设恢复复位状态。`CONFIG_INIT_ARCH_HW_AT_BOOT` 让 Zephyr 启动时，按相应 Arm 架构手册把内部 Cortex-M 架构状态初始化为复位值。

### 25.8.2\_软件向量转发

实现 VTOR 的平台用 `CONFIG_CPU_CORTEX_M_HAS_VTOR` 标记，链式镜像通过更新 VTOR 指向镜像向量表来重定位异常入口。

没有 VTOR 的 Baseline 平台，向量表可能固定，无法硬件重定位，需要软件转发。引导镜像启用 `CONFIG_SW_VECTOR_RELAY`，按应用设置的向量表指针转发异常与中断；应用启用 `CONFIG_SW_VECTOR_RELAY_CLIENT`，启动时在 SRAM 设置该指针，使引导程序转交至应用软件向量表。

该机制主要为无 VTOR 处理器设计，也可用于 Mainline 平台。

### 25.8.3\_重定位与链接脚本

启用 `CONFIG_CODE_DATA_RELOCATION_SRAM` 可把指定文件的 `.text`、`.data`、`.bss` 放进 SRAM，也可只移动部分段，无须移动整个镜像。详见[代码与数据重定位](../kernel/P050_代码与数据重定位.md)。

多数 Cortex-M 平台使用默认 GCC 链接脚本 `include/zephyr/arch/arm/cortex_m/scripts/linker.ld`，也允许平台采用自定义脚本。

### 25.8.4\_CMSIS

Cortex-M 的 CMSIS 头文件由独立模块提供：[CMSIS 5](https://github.com/zephyrproject-rtos/cmsis) 与 [CMSIS 6](https://github.com/zephyrproject-rtos/CMSIS_6)。

Zephyr 已开始把 Cortex-M 核心头文件默认来源迁向 CMSIS 6，但原文说明当前仍同时纳入 CMSIS 6 与旧 CMSIS 5 头文件。旧版本主要用于兼容厂商 HAL，新架构层开发应尽可能使用 CMSIS 6。

`CONFIG_CPU_CORTEX_M` 选择 `CONFIG_HAS_CMSIS_CORE`，表明所有受支持 Cortex-M 变体都可使用 CMSIS 核心头文件。

## 25.9\_测试与QEMU

架构及相关功能测试位于 `tests/arch/arm/`，测试集合不断扩展以增加覆盖。

Zephyr 通过多个 QEMU 目标验证 Cortex-M 架构功能，各目标有特定架构和模拟外设集合。以下完整保留原文支持矩阵：

| 模拟能力 | qemu_cortex_m0 | qemu_cortex_m3 | mps2/an385 | mps2/an521/cpu0 | mps3/corstone300/an547 |
| --- | --- | --- | --- | --- | --- |
| 架构 | Arm v6-M | Arm v7-M | Arm v7-M | Arm v8-M | Arm v8.1-M |
| NVIC | Y | Y | Y | Y | Y |
| BASEPRI | N | Y | Y | Y | Y |
| SysTick | N | Y | Y | Y | Y |
| MPU | N | N | Y | Y | Y |
| FPU | N | N | N | Y | N |
| SPLIM | N | N | N | Y | Y |
| TrustZone-M | N | N | N | Y | N |

> 译注：表格描述原文所列 QEMU 目标，不代表所有同名核心的真实芯片配置。本次只核对译文，没有执行 QEMU 测试。

## 25.10\_维护状态

原文标记 Cortex-M 移植为“有人维护”（maintained）。维护者与协作者的更新名单见项目 `MAINTAINERS.yml`。

---

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：内存屏障](P024_内存屏障.md) · [本模块主线目录](../reading/hardware.md) · [全部主线](../reading/README.md) · [下一篇：半主机](P026_半主机.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：内存屏障](P024_内存屏障.md) · [下一章：半主机](P026_半主机.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
