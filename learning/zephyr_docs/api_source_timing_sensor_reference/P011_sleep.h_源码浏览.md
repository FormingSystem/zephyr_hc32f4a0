---
id: learning.zephyr-docs.api-source-timing-sensor-reference.page-11
title: sleep.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sleep_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_sleep.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/sleep_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_reference/P400_zephyr__sleep.h_文件参考.md)。

## 11.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
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
<a id="l00030"></a>
<a id="l00048"></a>
<a id="l00049"></a>
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
<a id="l00188"></a>
<a id="foldopen00204"></a>
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
<a id="foldopen00227"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="foldopen00248"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="aclock_8h_html"></a>
<a id="agroup__clock__apis_html_ga222f9dff749accf8de62bc4b52c7bdcd"></a>
<a id="agroup__clock__apis_html_ga2d66311052e2bddf914610fb7345ff27"></a>
<a id="agroup__clock__apis_html_ga66e180b3d8940c30786a1d972cbd6d8d"></a>
<a id="agroup__clock__apis_html_ga6a69d6cbdab5f24c2e66959293f210c1"></a>
<a id="agroup__clock__apis_html_ga9832cb0adc2d1866420e5c370a0863e2"></a>
<a id="agroup__clock__apis_html_ga9abf00b34e16ab7ad0883603b6778b1b"></a>
<a id="agroup__sys-util_html_ga111fe4e9d63758262fc6810a782cb32a"></a>
<a id="agroup__sys-util_html_ga3acffbd305ee72dcd4593c0d8af64a4f"></a>
<a id="agroup__sys-util_html_gae664e7492e37d324831caf2321ddda37"></a>
<a id="agroup__thread__apis_html_ga093ac91db17ec33696168801d01efe75"></a>
<a id="agroup__thread__apis_html_ga5ad6bcbcf89f9a9fbf6929388e2a7842"></a>
<a id="agroup__thread__apis_html_gab761f90082335d57e3c6cd4013c819e6"></a>
<a id="agroup__thread__apis_html_gac1f1470dec2e89b4cb8fd8c5433bd101"></a>
<a id="agroup__timeutil__unit__apis_html_gabee58122304820b36d601268eb4598e2"></a>
<a id="agroup__timeutil__unit__apis_html_gad1c6d9e60835c6c00960778395cdbacc"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a181807730d4a375f848ba139813ce04f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astructk__timeout__t_html"></a>
<a id="asys_2util_8h_html"></a>
<a id="atime__units_8h_html"></a>
<a id="atoolchain_8h_html"></a>

```c
/*
 * Copyright (c) 2018 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_SLEEP_H_
#define ZEPHYR_INCLUDE_SLEEP_H_


#include <stdint.h>

#include <zephyr/sys/clock.h>
#include <zephyr/sys/time_units.h>
#include <zephyr/sys/util.h>
#include <zephyr/toolchain.h>

#ifdef __cplusplus
extern "C" {
#endif


__syscall k_ticks_t k_sleep_ticks(k_timeout_t timeout);


/*
 * k_sleep() and k_usleep() below are inlined on top of k_sleep_ticks()
 * rather than being separate out of line entry points.  That way the compiler
 * sees both whether the requested duration is constant and whether the caller
 * actually cares about the returned value, and it can fold or discard the
 * unit conversions accordingly.  Those conversions are the sole reason many
 * small builds pull in the 64 bit division helper.
 *
 * For the callers that do use the returned value, the two converters below
 * keep the arithmetic 32 bit wide.  They first clamp in the tick domain,
 * against a bound computed at compile time, which is what makes the narrower
 * arithmetic safe.  It pays off because a compiler strength reduces a 32 bit
 * division by a constant into a multiply, yet calls the 64 bit division
 * helper for that same constant divisor in 64 bit.
 *
 * Where the tick rate makes the conversion a single division or a single
 * multiplication, that holds on any target.  The split forms are different:
 * they trade one division for two or three, which only wins where the one
 * they replace would have been a call to a helper.  A 64 bit target divides
 * in hardware, so it keeps the plain converter for those.
 *
 * The tick count handed to these converters always lies in the
 * [0, INT32_MAX] range, since k_sleep_ticks() derives it from a 32 bit
 * subtraction, so narrowing k_ticks_t to a uint32_t loses nothing.
 */

#define Z_SLEEP_TICK_HZ ((uint32_t)CONFIG_SYS_CLOCK_TICKS_PER_SEC)

/* True when the conversion reduces to a single division or multiplication,
 * needing none of the splits.
 */
#define Z_SLEEP_IS_SIMPLE(to_hz) \
        (Z_SLEEP_TICK_HZ % (to_hz) == 0 || (to_hz) % Z_SLEEP_TICK_HZ == 0)

/* Largest tick count whose value in to_hz units still fits in an int32_t. */
#define Z_SLEEP_MAX_TICKS(to_hz) ((uint64_t)INT32_MAX * Z_SLEEP_TICK_HZ / (to_hz))

/* True when (rem * to_hz + Z_SLEEP_TICK_HZ - 1) cannot overflow 32 bits,
 * knowing that rem is a remainder modulo Z_SLEEP_TICK_HZ.
 */
#define Z_SLEEP_NO_OVERFLOW(to_hz) \
        ((uint64_t)Z_SLEEP_TICK_HZ * ((to_hz) + 1U) <= UINT32_MAX)

/* Past the clamp, ceil(t * to_hz / hz) without exceeding 32 bits: split the
 * division so the whole seconds are scaled separately from the remainder.
 */
#define Z_SLEEP_SPLIT(t, to_hz)                                             \
        (((t) / Z_SLEEP_TICK_HZ) * (to_hz) +                                \
         DIV_ROUND_UP(((t) % Z_SLEEP_TICK_HZ) * (to_hz), Z_SLEEP_TICK_HZ))

static ALWAYS_INLINE int32_t z_sleep_ticks_to_int32_ms(k_ticks_t ticks)
{
        uint32_t t = (uint32_t)ticks;

        /* a split is not worth narrowing for where 64 bit division is cheap */
        if (IS_ENABLED(CONFIG_64BIT) && !Z_SLEEP_IS_SIMPLE(MSEC_PER_SEC)) {
                return (int32_t)MIN(k_ticks_to_ms_ceil64(t), (uint64_t)INT32_MAX);
        }

        if (Z_SLEEP_MAX_TICKS(MSEC_PER_SEC) < (uint64_t)INT32_MAX &&
            t > (uint32_t)Z_SLEEP_MAX_TICKS(MSEC_PER_SEC)) {
                return INT32_MAX;
        }

        /* a whole number of ticks per millisecond, 1:1 included */
        if (Z_SLEEP_TICK_HZ % MSEC_PER_SEC == 0) {
                return (int32_t)DIV_ROUND_UP(t, z_tmcvt_divisor(Z_SLEEP_TICK_HZ, MSEC_PER_SEC));
        }

        /* a whole number of milliseconds per tick */
        if (MSEC_PER_SEC % Z_SLEEP_TICK_HZ == 0) {
                return (int32_t)(t * z_tmcvt_divisor(MSEC_PER_SEC, Z_SLEEP_TICK_HZ));
        }

        if (Z_SLEEP_NO_OVERFLOW(MSEC_PER_SEC)) {
                return (int32_t)Z_SLEEP_SPLIT(t, MSEC_PER_SEC);
        }

        /* tick rate too high to be scaled in 32 bits at all */
        return (int32_t)MIN(k_ticks_to_ms_ceil64(t), (uint64_t)INT32_MAX);
}

/* Microseconds need one step more than milliseconds: a remainder times
 * USEC_PER_SEC overflows 32 bits for any tick rate above 4294 Hz, so scale
 * the remainder by USEC_PER_MSEC twice, carrying the first quotient over.
 * With A = rem * 1000 = q * hz + r, ceil(A * 1000 / hz) is exactly
 * q * 1000 + ceil(r * 1000 / hz), and r < hz keeps the second step in range.
 */
static ALWAYS_INLINE int32_t z_sleep_ticks_to_int32_us_split(uint32_t t)
{
        uint32_t sec = t / Z_SLEEP_TICK_HZ;
        uint32_t rem = (t % Z_SLEEP_TICK_HZ) * USEC_PER_MSEC;
        uint32_t q = rem / Z_SLEEP_TICK_HZ;
        uint32_t r = rem % Z_SLEEP_TICK_HZ;

        return (int32_t)(sec * USEC_PER_SEC + q * USEC_PER_MSEC +
                         DIV_ROUND_UP(r * USEC_PER_MSEC, Z_SLEEP_TICK_HZ));
}

static ALWAYS_INLINE int32_t z_sleep_ticks_to_int32_us(k_ticks_t ticks)
{
        uint32_t t = (uint32_t)ticks;

        /* a split is not worth narrowing for where 64 bit division is cheap */
        if (IS_ENABLED(CONFIG_64BIT) && !Z_SLEEP_IS_SIMPLE(USEC_PER_SEC)) {
                return (int32_t)MIN(k_ticks_to_us_ceil64(t), (uint64_t)INT32_MAX);
        }

        if (Z_SLEEP_MAX_TICKS(USEC_PER_SEC) < (uint64_t)INT32_MAX &&
            t > (uint32_t)Z_SLEEP_MAX_TICKS(USEC_PER_SEC)) {
                return INT32_MAX;
        }

        /* a whole number of ticks per microsecond, 1:1 included */
        if (Z_SLEEP_TICK_HZ % USEC_PER_SEC == 0) {
                return (int32_t)DIV_ROUND_UP(t, z_tmcvt_divisor(Z_SLEEP_TICK_HZ, USEC_PER_SEC));
        }

        /* a whole number of microseconds per tick */
        if (USEC_PER_SEC % Z_SLEEP_TICK_HZ == 0) {
                return (int32_t)(t * z_tmcvt_divisor(USEC_PER_SEC, Z_SLEEP_TICK_HZ));
        }

        if (Z_SLEEP_NO_OVERFLOW(USEC_PER_SEC)) {
                return (int32_t)Z_SLEEP_SPLIT(t, USEC_PER_SEC);
        }

        if (Z_SLEEP_NO_OVERFLOW(USEC_PER_MSEC)) {
                return z_sleep_ticks_to_int32_us_split(t);
        }

        /* tick rate too high to be scaled in 32 bits at all */
        return (int32_t)MIN(k_ticks_to_us_ceil64(t), (uint64_t)INT32_MAX);
}


static ALWAYS_INLINE int32_t k_sleep(k_timeout_t timeout)
{
        k_ticks_t ticks = k_sleep_ticks(timeout);

        /* k_sleep() still returns 32 bit milliseconds for compatibility */
        if (K_TIMEOUT_EQ(timeout, Z_FOREVER)) {
                return (int32_t)K_TICKS_FOREVER;
        }

        return z_sleep_ticks_to_int32_ms(ticks);
}

static ALWAYS_INLINE int32_t k_msleep(int32_t ms)
{
        return k_sleep(Z_TIMEOUT_MS(ms));
}

static ALWAYS_INLINE int32_t k_usleep(int32_t us)
{
        k_ticks_t ticks = k_sleep_ticks(Z_TIMEOUT_US(us));

        return z_sleep_ticks_to_int32_us(ticks);
}


#ifdef __cplusplus
}
#endif

#include <zephyr/syscalls/sleep.h>

#endif /* ZEPHYR_INCLUDE_SLEEP_H_ */
```

## 11.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2018 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 52 行

下方的 `k_sleep()` 和 `k_usleep()` 基于 `k_sleep_ticks()` 内联实现，而不是提供独立的非内联入口。这样，编译器既能判断请求时长是否为常量，也能判断调用方是否实际使用返回值，从而相应地折叠或删除单位换算。这些换算是许多小型构建引入 64 位除法辅助函数（division helper）的唯一原因。

对于确实使用返回值的调用方，下方两个转换函数将算术运算限制在 32 位宽度内。它们先在时钟节拍（tick）域内进行限幅（clamp），限幅上界在编译时计算，正是这一步保证了使用较窄位宽运算的安全性。这样做有益，是因为编译器会通过强度削减（strength reduction），将 32 位常量除法转换为乘法；而对同一个常量除数进行 64 位除法时，仍会调用 64 位除法辅助函数。

如果某个节拍频率使换算可以简化为一次除法或一次乘法，这项优化适用于任何目标平台。拆分形式（split forms）有所不同：它们将一次除法换成两次或三次除法，只有原先那次除法需要调用辅助函数时才有收益。64 位目标平台使用硬件除法，因此对这些情况仍保留普通转换函数。

传给这些转换函数的节拍数始终位于 `[0, INT32_MAX]` 范围内，因为 `k_sleep_ticks()` 通过 32 位减法计算该值，所以将 `k_ticks_t` 缩窄为 `uint32_t` 不会损失信息。

### 注释 3：原第 80 行

换算可简化为单次除法或乘法、不需要任何拆分时为真。

### 注释 4：原第 86 行

以 `to_hz` 为频率单位换算后，结果仍可用 `int32_t` 表示的最大节拍数（tick count）。

### 注释 5：原第 89 行

已知 `rem` 是对 `Z_SLEEP_TICK_HZ` 取模得到的余数，当 `(rem * to_hz + Z_SLEEP_TICK_HZ - 1)` 不会溢出 32 位时为真。

### 注释 6：原第 95 行

完成限幅后，在不超过 32 位范围的条件下计算 `ceil(t * to_hz / hz)`：拆分除法，分别缩放整秒部分和余数部分。

### 注释 7：原第 106 行

如果 64 位除法开销较小，就不值得为缩窄位宽而拆分计算。

### 注释 8：原第 116 行

每毫秒包含整数个节拍（ticks），包括 1:1 的情况。

### 注释 9：原第 121 行

每个节拍对应整数毫秒。

### 注释 10：原第 130 行

节拍频率过高，完全无法在 32 位范围内完成缩放。

### 注释 11：原第 134 行

微秒换算比毫秒换算多一步：节拍频率高于 4294 Hz 时，余数乘以 `USEC_PER_SEC` 会溢出 32 位，因此将余数连续两次乘以 `USEC_PER_MSEC` 进行缩放，并将第一次得到的商带入后续结果。令 `A = rem * 1000 = q * hz + r`，则 `ceil(A * 1000 / hz)` 恰好等于 `q * 1000 + ceil(r * 1000 / hz)`；由于 `r < hz`，第二步仍保持在可表示范围内。

### 注释 12：原第 155 行

如果 64 位除法开销较小，就不值得为缩窄位宽而拆分计算。

### 注释 13：原第 165 行

每微秒包含整数个节拍，包括 1:1 的情况。

### 注释 14：原第 170 行

每个节拍对应整数微秒。

### 注释 15：原第 183 行

节拍频率过高，完全无法在 32 位范围内完成缩放。

### 注释 16：原第 208 行

为保持兼容性，`k_sleep()` 仍以 32 位毫秒数返回结果。

### 注释 17：原第 263 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_SLEEP_H_`。

## 11.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_reference/P400_zephyr__sleep.h_文件参考.md)
- [stdint.h](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md)
- [zephyr/sys/clock.h](../timer_reference/P090_系统时钟头文件参考.md)
- [zephyr/sys/time_units.h](../timeutil_reference/P011_时间单位头文件参考.md)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [k_ticks_t](../timer_reference/P086_系统时钟公共接口.md#ga9832cb0adc2d1866420e5c370a0863e2)
- [k_sleep_ticks](../thread_core_reference/P001_线程公共接口.md#ga5ad6bcbcf89f9a9fbf6929388e2a7842)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [IS_ENABLED](../util_reference/P001_通用工具公共接口.md#ga111fe4e9d63758262fc6810a782cb32a)
- [MSEC_PER_SEC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#ga222f9dff749accf8de62bc4b52c7bdcd)
- [MIN](../util_reference/P001_通用工具公共接口.md#ga3acffbd305ee72dcd4593c0d8af64a4f)
- [k_ticks_to_ms_ceil64](../timeutil_reference/P007_时间单位辅助接口.md#gabee58122304820b36d601268eb4598e2)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [INT32_MAX](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a181807730d4a375f848ba139813ce04f)
- [DIV_ROUND_UP](../util_reference/P001_通用工具公共接口.md#gae664e7492e37d324831caf2321ddda37)
- [USEC_PER_MSEC](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__apis.html#ga2d66311052e2bddf914610fb7345ff27)
- [USEC_PER_SEC](../timer_reference/P086_系统时钟公共接口.md#ga6a69d6cbdab5f24c2e66959293f210c1)
- [k_ticks_to_us_ceil64](../timeutil_reference/P007_时间单位辅助接口.md#gad1c6d9e60835c6c00960778395cdbacc)
- [k_sleep](../thread_core_reference/P001_线程公共接口.md#ga093ac91db17ec33696168801d01efe75)
- [K_TIMEOUT_EQ](../timer_reference/P086_系统时钟公共接口.md#ga9abf00b34e16ab7ad0883603b6778b1b)
- [K_TICKS_FOREVER](../timer_reference/P086_系统时钟公共接口.md#ga66e180b3d8940c30786a1d972cbd6d8d)
- [k_msleep](../thread_core_reference/P001_线程公共接口.md#gac1f1470dec2e89b4cb8fd8c5433bd101)
- [k_usleep](../thread_core_reference/P001_线程公共接口.md#gab761f90082335d57e3c6cd4013c819e6)
- [clock.h](../timer_reference/P090_系统时钟头文件参考.md)
- [util.h](../util_reference/P002_通用工具头文件参考.md)
- [time_units.h](../timeutil_reference/P011_时间单位头文件参考.md)
- [toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)

---

[上一章](P010_pzem004t.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P012_sys_getopt.h_源码浏览.md)
