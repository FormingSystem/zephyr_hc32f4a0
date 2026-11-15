---
id: learning.zephyr-docs.api-source-timing-sensor-reference.page-5
title: interrupt_util.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/interrupt__util_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_interrupt\_util.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/interrupt__util_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P170_____w__zephyr__zephyr__subsys__testsuite__include__zephyr__interrupt_util.h_文件参考.md)。

## 5.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00295"></a>
<a id="l00296"></a>
<a id="aarch__interface_8h_html"></a>
<a id="aarm-gic_8h_html"></a>
<a id="agic_8h_html"></a>
<a id="agic_8h_html_a08291705f002f01687cf507abbb410dc"></a>
<a id="agic_8h_html_a5125b5f77951f0e882e002aac406beec"></a>
<a id="agic_8h_html_ae388207ec492448a22511cee6dcecedc"></a>
<a id="agic_8h_html_ae759ef6f311a7279db5e7ccd68c80863"></a>
<a id="agroup__arch-misc_html_gabb087b9e158824121212d65646ae4154"></a>
<a id="agroup__arch-smp_html_gad42138d41dff6a4aad8abf7d77fcd8b2"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="agroup__sys__io__mmio__apis_html_gafebb790883d604c1ddbdbbd8314876d7"></a>
<a id="agroup__ztest__assert_html_gaeebddde19012223e3d5e853a1dac3ac5"></a>
<a id="aintc__infineon__aurix_8h_html"></a>
<a id="aintc__infineon__aurix_8h_html_a431de8a889dcd8691221a2ec3f7cda89"></a>
<a id="ainterrupt__util_8h_html_a48fcf2be56c2b4cb0fb15d77c9194f89"></a>
<a id="aloapic_8h_html"></a>
<a id="aloapic_8h_html_a060a375336bf44c2dde9537d32f9416d"></a>
<a id="aloapic_8h_html_aeea0b064b955e73205f882cd80132455"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>

```c
/*
 * Copyright (c) 2018 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef INTERRUPT_UTIL_H_
#define INTERRUPT_UTIL_H_

#define k_str_out_count(s) k_str_out((s), sizeof(s) - 1);

#if defined(CONFIG_CPU_CORTEX_M)
#include <cmsis_core.h>

static inline uint32_t get_available_nvic_line(uint32_t initial_offset)
{
        int i;

        for (i = initial_offset - 1; i >= 0; i--) {

                if (NVIC_GetEnableIRQ(i) == 0) {
                        /*
                         * Interrupts configured statically with IRQ_CONNECT(.)
                         * are automatically enabled. NVIC_GetEnableIRQ()
                         * returning false, here, implies that the IRQ line is
                         * either not implemented or it is not enabled, thus,
                         * currently not in use by Zephyr.
                         */

                        /* Set the NVIC line to pending. */
                        NVIC_SetPendingIRQ(i);

                        if (NVIC_GetPendingIRQ(i)) {
                                /*
                                 * If the NVIC line is pending, it is
                                 * guaranteed that it is implemented; clear the
                                 * line.
                                 */
                                NVIC_ClearPendingIRQ(i);

                                if (!NVIC_GetPendingIRQ(i)) {
                                        /*
                                         * If the NVIC line can be successfully
                                         * un-pended, it is guaranteed that it
                                         * can be used for software interrupt
                                         * triggering. Return the NVIC line
                                         * number.
                                         */
                                        break;
                                }
                        }
                }
        }

        zassert_true(i >= 0, "No available IRQ line\n");

        return i;
}

static inline void trigger_irq(int irq)
{
        k_str_out_count("Triggering irq\n");
#if defined(CONFIG_SOC_TI_LM3S6965_QEMU) || defined(CONFIG_CPU_CORTEX_M0) ||                       \
        defined(CONFIG_CPU_CORTEX_M0PLUS) || defined(CONFIG_CPU_CORTEX_M1) ||                      \
        defined(CONFIG_ARMV6_M_ARMV8_M_BASELINE)
        /* QEMU does not simulate the STIR register: this is a workaround */
        NVIC_SetPendingIRQ(irq);
#else
        NVIC->STIR = irq;
#endif
}

#elif defined(CONFIG_GIC)
#include <zephyr/drivers/interrupt_controller/gic.h>
#include <zephyr/dt-bindings/interrupt-controller/arm-gic.h>

static inline void trigger_irq(int irq)
{
        k_str_out_count("Triggering irq\n");

        /* Ensure that the specified IRQ number is a valid SGI interrupt ID */
        zassert_true(irq <= 15, "%u is not a valid SGI interrupt ID", irq);

        /*
         * Generate a software generated interrupt and forward it to the
         * requesting CPU.
         */
#if CONFIG_GIC_VER <= 2
        sys_write32(GICD_SGIR_TGTFILT_REQONLY | GICD_SGIR_SGIINTID(irq), GICD_SGIR);
#else
        uint64_t mpidr = GET_MPIDR();
        uint8_t aff0 = MPIDR_AFFLVL(mpidr, 0);

        gic_raise_sgi(irq, mpidr, BIT(aff0));
#endif
}

#elif defined(CONFIG_ARC)
static inline void trigger_irq(int irq)
{
        k_str_out_count("Triggering irq\n");
        z_arc_v2_aux_reg_write(_ARC_V2_AUX_IRQ_HINT, irq);
}

#elif defined(CONFIG_X86)

#ifdef CONFIG_X2APIC
#include <zephyr/drivers/interrupt_controller/loapic.h>
#define VECTOR_MASK 0xFF
#else
#include <zephyr/arch/arch_interface.h>
#define LOAPIC_ICR_IPI_TEST 0x00004000U
#endif

/*
 * We can emulate the interrupt by sending the IPI to
 * core itself by the LOAPIC for x86 platform.
 *
 * In APIC mode, Write LOAPIC's ICR to trigger IPI,
 * the LOAPIC_ICR_IPI_TEST  0x00004000U means:
 * Delivery Mode: Fixed
 * Destination Mode: Physical
 * Level: Assert
 * Trigger Mode: Edge
 * Destination Shorthand: No Shorthand
 * Destination: depends on cpu_id
 *
 * In X2APIC mode, this no longer works. We emulate the
 * interrupt by writing the IA32_X2APIC_SELF_IPI MSR
 * to send IPI to the core itself via LOAPIC also.
 * According to SDM vol.3 chapter 10.12.11, the bit[7:0]
 * for setting the vector is only needed.
 */
static inline void trigger_irq(int vector)
{
        uint8_t i;

#ifdef CONFIG_X2APIC
        x86_write_x2apic(LOAPIC_SELF_IPI, ((VECTOR_MASK & vector)));
#else

#ifdef CONFIG_SMP
        int cpu_id = arch_curr_cpu()->id;
#else
        int cpu_id = 0;
#endif
        z_loapic_ipi(cpu_id, LOAPIC_ICR_IPI_TEST, vector);
#endif /* CONFIG_X2APIC */

        /*
         * add some nop operations here to cost some cycles to make sure
         * the IPI interrupt is handled before do our check.
         */
        for (i = 0; i < 10; i++) {
                arch_nop();
        }
}

#elif defined(CONFIG_ARCH_POSIX)
#include <zephyr/arch/posix/posix_soc_if.h>

static inline void trigger_irq(int irq)
{
        posix_sw_set_pending_IRQ(irq);
}

#elif defined(CONFIG_RISCV)
#if defined(CONFIG_HAZARD3_INTC)
#include <hardware/irq.h>
#endif

#if defined(CONFIG_CLIC) || defined(CONFIG_NRFX_CLIC)
void riscv_clic_irq_set_pending(uint32_t irq);
static inline void trigger_irq(int irq)
{
        riscv_clic_irq_set_pending(irq);
}
#elif defined(CONFIG_HAZARD3_INTC)
static inline void trigger_irq(int irq)
{
        irq_set_pending(irq);
}
#elif defined(CONFIG_RISCV_S_MODE)
/* In S-mode mip is read-only; set bits via sip (SSIP is writable via sip) */
static inline void trigger_irq(int irq)
{
        uint32_t sip;

        __asm__ volatile("csrrs %0, sip, %1\n" : "=r"(sip) : "r"(1 << irq));
}
#else
static inline void trigger_irq(int irq)
{
        uint32_t mip;

        __asm__ volatile("csrrs %0, mip, %1\n" : "=r"(mip) : "r"(1 << irq));
}
#endif
#elif defined(CONFIG_XTENSA)
static inline void trigger_irq(int irq)
{
#if XCHAL_NUM_INTERRUPTS > 32
        switch (irq >> 5) {
        case 0:
                z_xt_set_intset(1 << (irq & 0x1f));
                break;
        case 1:
                z_xt_set_intset1(1 << (irq & 0x1f));
                break;
#if XCHAL_NUM_INTERRUPTS > 64
        case 2:
                z_xt_set_intset2(1 << (irq & 0x1f));
                break;
#endif
#if XCHAL_NUM_INTERRUPTS > 96
        case 3:
                z_xt_set_intset3(1 << (irq & 0x1f));
                break;
#endif
        default:
                break;
        }
#else
        z_xt_set_intset(1 << irq);
#endif
}

#elif defined(CONFIG_SPARC)
extern void z_sparc_enter_irq(int);

static inline void trigger_irq(int irq)
{
        z_sparc_enter_irq(irq);
}

#elif defined(CONFIG_MIPS)
extern void z_mips_enter_irq(int);

static inline void trigger_irq(int irq)
{
        z_mips_enter_irq(irq);
}

#elif defined(CONFIG_OPENRISC)
extern void z_openrisc_enter_irq(int);

static inline void trigger_irq(int irq)
{
        z_openrisc_enter_irq(irq);
}

#elif defined(CONFIG_CPU_CORTEX_R5) && defined(CONFIG_TI_VIM)

extern void z_vim_arm_enter_irq(int);

static inline void trigger_irq(int irq)
{
        z_vim_arm_enter_irq(irq);
}

#elif defined(CONFIG_RX)
#define IR_BASE_ADDRESS DT_REG_ADDR_BY_NAME(DT_NODELABEL(icu), IR)
static inline void trigger_irq(int irq)
{
        __ASSERT(irq < CONFIG_NUM_IRQS, "attempting to trigger invalid IRQ (%u)", irq);
        __ASSERT(irq >= CONFIG_GEN_IRQ_START_VECTOR, "attempting to trigger reserved IRQ (%u)",
                 irq);
        _sw_isr_table[irq - CONFIG_GEN_IRQ_START_VECTOR].isr(
                _sw_isr_table[irq - CONFIG_GEN_IRQ_START_VECTOR].arg);
}

#elif defined(CONFIG_HEXAGON)

/* Posts the interrupt through the Hexagon VM, the same hypercall the arch's
 * irq_offload() uses.
 */
extern int hexagon_irq_trigger(unsigned int irq);

static inline void trigger_irq(int irq)
{
        hexagon_irq_trigger((unsigned int)irq);
}

#elif defined(CONFIG_TRICORE)
#include <zephyr/drivers/interrupt_controller/intc_infineon_aurix.h>

static inline void trigger_irq(int irq)
{
        intc_aurix_ir_irq_raise(irq);
}

#else
#define NO_TRIGGER_FROM_SW
#endif

#endif /* INTERRUPT_UTIL_H_ */
```

## 5.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2018 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 22 行

使用 `IRQ_CONNECT(.)` 静态配置的中断会自动启用。此处 `NVIC_GetEnableIRQ()` 返回 false，表示该中断请求（IRQ）线未实现或未启用，因此当前未被 Zephyr 使用。

### 注释 3：原第 30 行

将嵌套向量中断控制器（NVIC）的中断线设为挂起（pending）。

### 注释 4：原第 34 行

如果 NVIC 中断线处于挂起状态，就能确定它已实现；随后清除该中断线的挂起状态。

### 注释 5：原第 42 行

如果能够成功取消 NVIC 中断线的挂起状态，就能确定它可用于软件中断触发（software interrupt triggering）。返回该 NVIC 中断线编号。

### 注释 6：原第 66 行

QEMU 不模拟软件触发中断寄存器（STIR）；此处提供变通处理（workaround）。

### 注释 7：原第 81 行

确保指定的 IRQ 编号是有效的软件生成中断（SGI）标识符。

### 注释 8：原第 84 行

产生一个软件生成中断（software generated interrupt），并将其转发给发起请求的 CPU。

### 注释 9：原第 115 行

在 x86 平台上，可以通过本地 APIC（LOAPIC）向核心自身发送处理器间中断（IPI）来模拟中断。

在 APIC 模式下，写入 LOAPIC 的中断命令寄存器（ICR）以触发 IPI。`LOAPIC_ICR_IPI_TEST` 的值 `0x00004000U` 表示：

- 投递模式（Delivery Mode）：固定（Fixed）。
- 目标模式（Destination Mode）：物理（Physical）。
- 电平（Level）：置位（Assert）。
- 触发模式（Trigger Mode）：边沿（Edge）。
- 目标简写（Destination Shorthand）：不使用简写（No Shorthand）。
- 目标（Destination）：取决于 `cpu_id`。

在 X2APIC 模式下，上述方式不再有效。改为写入 `IA32_X2APIC_SELF_IPI` 模型专用寄存器（MSR），同样通过 LOAPIC 向核心自身发送 IPI 来模拟中断。根据软件开发者手册（SDM）第 3 卷第 10.12.11 节，只需设置用于指定向量的位 `[7:0]`。

### 注释 10：原第 148 行

条件编译配置（Configuration）标记：`CONFIG_X2APIC`。

### 注释 11：原第 150 行

此处加入一些空操作（nop）以消耗若干周期，确保检查之前 IPI 中断已经得到处理。

### 注释 12：原第 184 行

在监管者模式（S-mode）下，`mip` 只读；应通过 `sip` 设置位，SSIP 可通过 `sip` 写入。

### 注释 13：原第 274 行

通过 Hexagon 虚拟机（VM）提交中断，使用与该架构 `irq_offload()` 相同的超级调用（hypercall）。

### 注释 14：原第 296 行

头文件保护宏（Header guard）标记：`INTERRUPT_UTIL_H_`。

## 5.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P170_____w__zephyr__zephyr__subsys__testsuite__include__zephyr__interrupt_util.h_文件参考.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [zassert_true](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__assert.html#gaeebddde19012223e3d5e853a1dac3ac5)
- [k_str_out_count](../api_file_reference/P170_____w__zephyr__zephyr__subsys__testsuite__include__zephyr__interrupt_util.h_文件参考.md#a48fcf2be56c2b4cb0fb15d77c9194f89)
- [zephyr/drivers/interrupt_controller/gic.h](https://docs.zephyrproject.org/latest/doxygen/html/gic_8h.html)
- [zephyr/dt-bindings/interrupt-controller/arm-gic.h](https://docs.zephyrproject.org/latest/doxygen/html/arm-gic_8h.html)
- [sys_write32](../device_reference/P019_内存映射寄存器IO接口.md#gafebb790883d604c1ddbdbbd8314876d7)
- [GICD_SGIR_TGTFILT_REQONLY](https://docs.zephyrproject.org/latest/doxygen/html/gic_8h.html#ae759ef6f311a7279db5e7ccd68c80863)
- [GICD_SGIR_SGIINTID](https://docs.zephyrproject.org/latest/doxygen/html/gic_8h.html#ae388207ec492448a22511cee6dcecedc)
- [GICD_SGIR](https://docs.zephyrproject.org/latest/doxygen/html/gic_8h.html#a5125b5f77951f0e882e002aac406beec)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [gic_raise_sgi](https://docs.zephyrproject.org/latest/doxygen/html/gic_8h.html#a08291705f002f01687cf507abbb410dc)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [zephyr/drivers/interrupt_controller/loapic.h](https://docs.zephyrproject.org/latest/doxygen/html/loapic_8h.html)
- [zephyr/arch/arch_interface.h](https://docs.zephyrproject.org/latest/doxygen/html/arch__interface_8h.html)
- [x86_write_x2apic](https://docs.zephyrproject.org/latest/doxygen/html/loapic_8h.html#a060a375336bf44c2dde9537d32f9416d)
- [LOAPIC_SELF_IPI](https://docs.zephyrproject.org/latest/doxygen/html/loapic_8h.html#aeea0b064b955e73205f882cd80132455)
- [arch_curr_cpu](../arch_core_reference/P005_架构多处理器接口.md#gad42138d41dff6a4aad8abf7d77fcd8b2)
- [arch_nop](../arch_core_reference/P008_架构杂项接口.md#gabb087b9e158824121212d65646ae4154)
- [zephyr/drivers/interrupt_controller/intc_infineon_aurix.h](https://docs.zephyrproject.org/latest/doxygen/html/intc__infineon__aurix_8h.html)
- [intc_aurix_ir_irq_raise](https://docs.zephyrproject.org/latest/doxygen/html/intc__infineon__aurix_8h.html#a431de8a889dcd8691221a2ec3f7cda89)
- [arch_interface.h](https://docs.zephyrproject.org/latest/doxygen/html/arch__interface_8h.html)
- [arm-gic.h](https://docs.zephyrproject.org/latest/doxygen/html/arm-gic_8h.html)
- [gic.h](https://docs.zephyrproject.org/latest/doxygen/html/gic_8h.html)
- [intc_infineon_aurix.h](https://docs.zephyrproject.org/latest/doxygen/html/intc__infineon__aurix_8h.html)
- [loapic.h](https://docs.zephyrproject.org/latest/doxygen/html/loapic_8h.html)

---

[上一章](P004_ifx_clock_source_pse8xx.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P006_libc-hooks.h_源码浏览.md)
