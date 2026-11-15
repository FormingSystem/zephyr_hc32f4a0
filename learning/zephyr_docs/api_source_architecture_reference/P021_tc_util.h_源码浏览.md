---
id: learning.zephyr-docs.api-source-architecture-reference.page-21
title: tc_util.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/tc__util_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_tc\_util.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/tc__util_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/tc__util_8h.html)。

## 21.1\_原始可见代码（Source Code）

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
<a id="foldopen00071"></a>
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
<a id="foldopen00100"></a>
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
<a id="foldopen00119"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="foldopen00124"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="foldopen00132"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="foldopen00139"></a>
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
<a id="foldopen00165"></a>
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
<a id="foldopen00194"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="foldopen00199"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="foldopen00208"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="foldopen00216"></a>
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
<a id="foldopen00237"></a>
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
<a id="foldopen00260"></a>
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
<a id="agroup__clock__apis_html_ga208687de625e0036558343b4e66143d3"></a>
<a id="agroup__timeutil__unit__apis_html_ga40bf11b01ba76673c67569e8d1e55d92"></a>
<a id="akernel_8h_html"></a>
<a id="alog__ctrl_8h_html"></a>
<a id="aprintk_8h_html"></a>
<a id="ashell_2shell_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astring_8h_html"></a>
<a id="atc__util_8h_html_a196c300c18de32c79d757131b579a3a5"></a>
<a id="atc__util_8h_html_a30c304c5caa2145085e83fdbd5fa24e4"></a>
<a id="atc__util_8h_html_a497dd92db8a77681994baee1ba3f0847"></a>
<a id="atc__util_8h_html_a584cf09eac3d2fa3758924cb843cdbf5"></a>
<a id="atc__util_8h_html_a586f060684ebfc5db4105a30370a41d0"></a>
<a id="atc__util_8h_html_a991995992ef5c23b7c6cf7138b394437"></a>
<a id="atc__util_8h_html_a9bb8eafa6af5b875097421ba21a8dfc8"></a>
<a id="atc__util_8h_html_a9e2302e8d62cfefe7df86e62489efe29"></a>
<a id="atc__util_8h_html_ab6f8f2a5ffd8240715e1eef0dfd27907"></a>
<a id="atc__util_8h_html_abafb6d8cf1e1a3bb2247d5384d1d5461"></a>
<a id="atc__util_8h_html_ac0108c70de44b3186c7ead1c1430b3d1"></a>
<a id="atc__util_8h_html_ac5103b154fa450c478c2bf3f520cb8ff"></a>
<a id="atc__util_8h_html_ad3aec479c61df7656ae28f68aa4dc4a5"></a>
<a id="atc__util_8h_html_afb66a88e5d1e781aeb5aa9739a8fe868"></a>

```c
/* tc_utilities.h - testcase utilities header file */

/*
 * Copyright (c) 2012-2015 Wind River Systems, Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_TESTSUITE_INCLUDE_TC_UTIL_H_
#define ZEPHYR_TESTSUITE_INCLUDE_TC_UTIL_H_

#include <zephyr/kernel.h>

#include <string.h>
#ifdef CONFIG_SHELL
#include <zephyr/shell/shell.h>
#endif
#include <zephyr/sys/printk.h>

#if defined CONFIG_ZTEST_TC_UTIL_USER_OVERRIDE
#include <tc_util_user_override.h>
#endif

#ifndef PRINT_DATA
#define PRINT_DATA(fmt, ...) printk(fmt, ##__VA_ARGS__)
#endif

#if defined CONFIG_ARCH_POSIX
#include <posix_board_if.h>
#endif

#define TC_STR_HELPER(x) #x
#define TC_STR(x) TC_STR_HELPER(x)
#ifdef TC_RUNID
#define TC_PRINT_RUNID PRINT_DATA("RunID: " TC_STR(TC_RUNID) "\n")
#define TC_PRINT_RUNID_START PRINT_DATA("RunID started: " TC_STR(TC_RUNID) "\n")
#else
#define TC_PRINT_RUNID do {} while (false)
#define TC_PRINT_RUNID_START do {} while (false)
#endif

#ifndef PRINT_LINE
#define PRINT_LINE                          \
        PRINT_DATA(                                                        \
                "============================================================" \
                "=======\n")
#endif

/* stack size and priority for test suite task */
#define TASK_STACK_SIZE (1024 * 2)

#define FMT_ERROR "%s - %s@%d. "

#define TC_PASS 0
#define TC_FAIL 1
#define TC_SKIP 2
#define TC_FLAKY 3

#ifndef TC_PASS_STR
#define TC_PASS_STR "PASS"
#endif
#ifndef TC_FAIL_STR
#define TC_FAIL_STR "FAIL"
#endif
#ifndef TC_SKIP_STR
#define TC_SKIP_STR "SKIP"
#endif
#ifndef TC_FLAKY_STR
#define TC_FLAKY_STR "FLAKY"
#endif

static inline const char *TC_RESULT_TO_STR(int result)
{
        switch (result) {
        case TC_PASS:
                return TC_PASS_STR;
        case TC_FAIL:
                return TC_FAIL_STR;
        case TC_SKIP:
                return TC_SKIP_STR;
        case TC_FLAKY:
                return TC_FLAKY_STR;
        default:
                return "?";
        }
}

static uint32_t tc_start_time;
static uint32_t tc_spend_time;

static inline void get_start_time_cyc(void)
{
        tc_start_time = k_cycle_get_32();
}

static inline void get_test_duration_ms(void)
{
        uint32_t spend_cycle = k_cycle_get_32() - tc_start_time;

        tc_spend_time = k_cyc_to_ms_ceil32(spend_cycle);
}

#ifndef TC_ERROR
#define TC_ERROR(fmt, ...)                               \
        do {                                                 \
                PRINT_DATA(FMT_ERROR, "FAIL", __func__, __LINE__); \
                PRINT_DATA(fmt, ##__VA_ARGS__);                  \
        } while (false)
#endif

static inline void print_nothing(const char *fmt, ...)
{
        ARG_UNUSED(fmt);
}

#ifndef TC_PRINT
#if defined(CONFIG_ZTEST_VERBOSE_OUTPUT)
#define TC_PRINT(fmt, ...) PRINT_DATA(fmt, ##__VA_ARGS__)
#else
#define TC_PRINT(fmt, ...) print_nothing(fmt, ##__VA_ARGS__)
#endif /* CONFIG_ZTEST_VERBOSE_OUTPUT */
#endif /* TC_PRINT */

#ifndef TC_SUMMARY_PRINT
#define TC_SUMMARY_PRINT(fmt, ...) PRINT_DATA(fmt, ##__VA_ARGS__)
#endif

#ifndef TC_START_PRINT
#if defined(CONFIG_ZTEST_VERBOSE_OUTPUT)
#define TC_START_PRINT(name) PRINT_DATA("START - %s\n", name);
#else
#define TC_START_PRINT(name) print_nothing(name)
#endif /* CONFIG_ZTEST_VERBOSE_OUTPUT */
#endif /* TC_START_PRINT */

#ifndef TC_START
#define TC_START(name)                                                  \
        do {                                                            \
                TC_START_PRINT(name);                   \
        } while (0)
#endif

#ifndef TC_END
#define TC_END(result, fmt, ...) PRINT_DATA(fmt, ##__VA_ARGS__)
#endif

#ifndef TC_END_PRINT
#if defined(CONFIG_ZTEST_VERBOSE_OUTPUT)
#define TC_END_PRINT(result, fmt, ...) PRINT_DATA(fmt, ##__VA_ARGS__); PRINT_LINE
#else
#define TC_END_PRINT(result, fmt, ...) print_nothing(fmt)
#endif /* CONFIG_ZTEST_VERBOSE_OUTPUT */
#endif /* TC_END_PRINT */

/* prints result and the function name */
#ifndef Z_TC_END_RESULT
#define Z_TC_END_RESULT(result, func)                                           \
        do {                                                                    \
                TC_END_PRINT(result, " %s - %s in %u.%03u seconds\n",           \
                        TC_RESULT_TO_STR(result), func, tc_spend_time/1000,     \
                        tc_spend_time%1000);                                    \
        } while (0)
#endif

#ifndef TC_END_RESULT
#define TC_END_RESULT(result)                           \
        Z_TC_END_RESULT((result), __func__)
#endif

#ifndef TC_END_RESULT_CUSTOM
#define TC_END_RESULT_CUSTOM(result, func)                           \
        Z_TC_END_RESULT((result), func)
#endif

#ifndef TC_SUITE_PRINT
#define TC_SUITE_PRINT(fmt, ...) PRINT_DATA(fmt, ##__VA_ARGS__)
#endif

#ifndef TC_SUITE_START
#define TC_SUITE_START(name)                                    \
        do {                                                    \
                TC_SUITE_PRINT("Running TESTSUITE %s\n", name); \
                PRINT_LINE;                                     \
        } while (false)
#endif

#ifndef TC_SUITE_END
#define TC_SUITE_END(name, result)                              \
        do {                                                            \
                if (result != TC_FAIL) {                                \
                        TC_SUITE_PRINT("TESTSUITE %s succeeded\n", name);       \
                } else {                                                \
                        TC_SUITE_PRINT("TESTSUITE %s failed.\n", name); \
                }                                                       \
        } while (false)
#endif

#if defined(CONFIG_ARCH_POSIX) && !defined(CONFIG_ZTEST_SHELL)
#include <zephyr/logging/log_ctrl.h>
#define TC_END_POST(result) do { \
        LOG_PANIC(); \
        posix_exit(result); \
} while (0)
#else
#define TC_END_POST(result)
#endif /* CONFIG_ARCH_POSIX */

#ifndef TC_END_REPORT
#define TC_END_REPORT(result)                               \
        do {                                                    \
                PRINT_LINE;                                         \
                TC_PRINT_RUNID;                                         \
                TC_END(result,                                      \
                       "PROJECT EXECUTION %s\n",               \
                       (result) == TC_PASS ? "SUCCESSFUL" : "FAILED");  \
                TC_END_POST(result);                                    \
        } while (false)
#endif

#if defined(CONFIG_SHELL)
#define TC_CMD_DEFINE(name)                                             \
        static int cmd_##name(const struct shell *sh, size_t argc,      \
                              char **argv) \
        {                                                               \
                TC_START(__func__);                                     \
                name();                                                 \
                TC_END_RESULT(TC_PASS);                                 \
                return 0;                                               \
        }
#define TC_CMD_ITEM(name)       cmd_##name
#else
#define TC_CMD_DEFINE(name)                             \
        int cmd_##name(int argc, char *argv[])          \
        {                                               \
                TC_START(__func__);                     \
                name();                                 \
                TC_END_RESULT(TC_PASS);                 \
                return 0;                               \
        }
#define TC_CMD_ITEM(name) {STRINGIFY(name), cmd_##name, "none"}
#endif

#endif /* ZEPHYR_TESTSUITE_INCLUDE_TC_UTIL_H_ */
```

## 21.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

`tc_utilities.h`：测试用例工具头文件（Testcase Utilities Header File）。

### 注释 2：原第 3 行

版权（Copyright）：© 2012-2015 Wind River Systems, Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 3：原第 77 行

测试套件任务（Test Suite Task）的栈大小（Stack Size）和优先级（Priority）。

### 注释 4：原第 149 行

条件编译配置（Configuration）标记：`CONFIG_ZTEST_VERBOSE_OUTPUT`。

### 注释 5：原第 150 行

测试输出宏（Test Print Macro）：`TC_PRINT`。

### 注释 6：原第 161 行

条件编译配置（Configuration）标记：`CONFIG_ZTEST_VERBOSE_OUTPUT`。

### 注释 7：原第 162 行

测试开始输出宏（Test Start Print Macro）：`TC_START_PRINT`。

### 注释 8：原第 180 行

条件编译配置（Configuration）标记：`CONFIG_ZTEST_VERBOSE_OUTPUT`。

### 注释 9：原第 181 行

测试结束输出宏（Test End Print Macro）：`TC_END_PRINT`。

### 注释 10：原第 183 行

打印结果（Result）和函数名称（Function Name）。

### 注释 11：原第 234 行

条件编译配置（Configuration）标记：`CONFIG_ARCH_POSIX`。

### 注释 12：原第 271 行

头文件保护宏（Header guard）标记：`ZEPHYR_TESTSUITE_INCLUDE_TC_UTIL_H_`。

## 21.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/tc__util_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [string.h](../api_file_reference/P472_____w__zephyr__zephyr__lib__libc__minimal__include__string.h_文件参考.md)
- [zephyr/shell/shell.h](../shell_core_reference/P002_Shell核心头文件参考.md)
- [zephyr/sys/printk.h](https://docs.zephyrproject.org/latest/doxygen/html/printk_8h.html)
- [TC_RESULT_TO_STR](https://docs.zephyrproject.org/latest/doxygen/html/tc__util_8h.html#a9e2302e8d62cfefe7df86e62489efe29)
- [TC_PASS](https://docs.zephyrproject.org/latest/doxygen/html/tc__util_8h.html#afb66a88e5d1e781aeb5aa9739a8fe868)
- [TC_PASS_STR](https://docs.zephyrproject.org/latest/doxygen/html/tc__util_8h.html#a991995992ef5c23b7c6cf7138b394437)
- [TC_FAIL](https://docs.zephyrproject.org/latest/doxygen/html/tc__util_8h.html#a196c300c18de32c79d757131b579a3a5)
- [TC_FAIL_STR](https://docs.zephyrproject.org/latest/doxygen/html/tc__util_8h.html#ac5103b154fa450c478c2bf3f520cb8ff)
- [TC_SKIP](https://docs.zephyrproject.org/latest/doxygen/html/tc__util_8h.html#abafb6d8cf1e1a3bb2247d5384d1d5461)
- [TC_SKIP_STR](https://docs.zephyrproject.org/latest/doxygen/html/tc__util_8h.html#a586f060684ebfc5db4105a30370a41d0)
- [TC_FLAKY](https://docs.zephyrproject.org/latest/doxygen/html/tc__util_8h.html#ac0108c70de44b3186c7ead1c1430b3d1)
- [TC_FLAKY_STR](https://docs.zephyrproject.org/latest/doxygen/html/tc__util_8h.html#a584cf09eac3d2fa3758924cb843cdbf5)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [tc_start_time](https://docs.zephyrproject.org/latest/doxygen/html/tc__util_8h.html#ad3aec479c61df7656ae28f68aa4dc4a5)
- [tc_spend_time](https://docs.zephyrproject.org/latest/doxygen/html/tc__util_8h.html#a9bb8eafa6af5b875097421ba21a8dfc8)
- [get_start_time_cyc](https://docs.zephyrproject.org/latest/doxygen/html/tc__util_8h.html#a497dd92db8a77681994baee1ba3f0847)
- [k_cycle_get_32](../timer_reference/P086_系统时钟公共接口.md#ga208687de625e0036558343b4e66143d3)
- [get_test_duration_ms](https://docs.zephyrproject.org/latest/doxygen/html/tc__util_8h.html#ab6f8f2a5ffd8240715e1eef0dfd27907)
- [k_cyc_to_ms_ceil32](../timeutil_reference/P007_时间单位辅助接口.md#ga40bf11b01ba76673c67569e8d1e55d92)
- [print_nothing](https://docs.zephyrproject.org/latest/doxygen/html/tc__util_8h.html#a30c304c5caa2145085e83fdbd5fa24e4)
- [zephyr/logging/log_ctrl.h](../log_core_reference/P006_日志控制头文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [log_ctrl.h](../log_core_reference/P006_日志控制头文件参考.md)
- [printk.h](https://docs.zephyrproject.org/latest/doxygen/html/printk_8h.html)
- [shell.h](../shell_core_reference/P002_Shell核心头文件参考.md)

---

[上一章](P020_sections.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P022_uart_ifx_cat1.h_源码浏览.md)
