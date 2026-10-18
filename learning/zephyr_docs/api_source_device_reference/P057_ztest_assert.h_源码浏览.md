---
id: learning.zephyr-docs.api-source-device-reference.page-57
title: ztest_assert.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ztest__assert_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第57章\_ztest\_assert.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ztest__assert_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ztest__assert_8h.html)。

## 57.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
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
<a id="l00187"></a>
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
<a id="foldopen00218"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
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
<a id="foldopen00255"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00257"></a>
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
<a id="foldopen00284"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="l00305"></a>
<a id="l00306"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="foldopen00326"></a>
<a id="l00326"></a>
<a id="l00327"></a>
<a id="l00328"></a>
<a id="foldopen00334"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="l00346"></a>
<a id="l00347"></a>
<a id="l00357"></a>
<a id="l00358"></a>
<a id="foldopen00368"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="l00370"></a>
<a id="foldopen00379"></a>
<a id="l00379"></a>
<a id="l00380"></a>
<a id="l00381"></a>
<a id="l00382"></a>
<a id="foldopen00392"></a>
<a id="l00392"></a>
<a id="l00393"></a>
<a id="l00394"></a>
<a id="l00395"></a>
<a id="l00407"></a>
<a id="l00408"></a>
<a id="foldopen00420"></a>
<a id="l00420"></a>
<a id="l00421"></a>
<a id="l00422"></a>
<a id="foldopen00430"></a>
<a id="l00430"></a>
<a id="l00431"></a>
<a id="l00432"></a>
<a id="l00436"></a>
<a id="l00445"></a>
<a id="l00454"></a>
<a id="l00455"></a>
<a id="l00464"></a>
<a id="l00465"></a>
<a id="l00474"></a>
<a id="l00475"></a>
<a id="l00484"></a>
<a id="l00485"></a>
<a id="foldopen00494"></a>
<a id="l00494"></a>
<a id="l00495"></a>
<a id="l00496"></a>
<a id="foldopen00505"></a>
<a id="l00505"></a>
<a id="l00506"></a>
<a id="l00507"></a>
<a id="l00518"></a>
<a id="l00519"></a>
<a id="l00530"></a>
<a id="l00531"></a>
<a id="foldopen00542"></a>
<a id="l00542"></a>
<a id="l00543"></a>
<a id="l00544"></a>
<a id="foldopen00555"></a>
<a id="l00555"></a>
<a id="l00556"></a>
<a id="l00557"></a>
<a id="l00558"></a>
<a id="foldopen00570"></a>
<a id="l00570"></a>
<a id="l00571"></a>
<a id="l00572"></a>
<a id="l00573"></a>
<a id="l00585"></a>
<a id="l00586"></a>
<a id="foldopen00600"></a>
<a id="l00600"></a>
<a id="l00601"></a>
<a id="l00602"></a>
<a id="foldopen00610"></a>
<a id="l00610"></a>
<a id="l00611"></a>
<a id="l00612"></a>
<a id="l00616"></a>
<a id="l00625"></a>
<a id="l00632"></a>
<a id="l00633"></a>
<a id="l00640"></a>
<a id="l00641"></a>
<a id="l00649"></a>
<a id="l00650"></a>
<a id="l00658"></a>
<a id="l00659"></a>
<a id="foldopen00666"></a>
<a id="l00666"></a>
<a id="l00667"></a>
<a id="l00668"></a>
<a id="foldopen00675"></a>
<a id="l00675"></a>
<a id="l00676"></a>
<a id="l00677"></a>
<a id="l00685"></a>
<a id="l00686"></a>
<a id="l00697"></a>
<a id="l00698"></a>
<a id="foldopen00708"></a>
<a id="l00708"></a>
<a id="l00709"></a>
<a id="l00710"></a>
<a id="foldopen00720"></a>
<a id="l00720"></a>
<a id="l00721"></a>
<a id="l00722"></a>
<a id="l00723"></a>
<a id="foldopen00733"></a>
<a id="l00733"></a>
<a id="l00734"></a>
<a id="l00735"></a>
<a id="l00736"></a>
<a id="foldopen00746"></a>
<a id="l00746"></a>
<a id="l00747"></a>
<a id="l00748"></a>
<a id="foldopen00757"></a>
<a id="l00757"></a>
<a id="l00758"></a>
<a id="l00759"></a>
<a id="l00763"></a>
<a id="l00764"></a>
<a id="l00765"></a>
<a id="l00766"></a>
<a id="l00767"></a>
<a id="l00768"></a>
<a id="aprintk_8h_html_a1bce54a738ce2d9dd6d95ee842ec237c"></a>
<a id="aprintk_8h_html_a9b5fa01884b98d143218af0cd0ffe841"></a>
<a id="astdbool_8h_html"></a>
<a id="astdbool_8h_html_abb452686968e48b67397da5f97445f5b"></a>
<a id="astdio_8h_html"></a>
<a id="astring_8h_html"></a>
<a id="asys_2util_8h_html"></a>
<a id="atc__util_8h_html"></a>
<a id="atc__util_8h_html_aec98e66470b575771ed484118095b692"></a>
<a id="aztest_8h_html"></a>
<a id="aztest__assert_8h_html_a06a081e3d716be7e024973cbf305c14b"></a>
<a id="aztest__assert_8h_html_a17537c79021fbc12e56b72ccec4b99c5"></a>
<a id="aztest__assert_8h_html_a5c6bb493c88f7426a827889526dc0772"></a>
<a id="aztest__assert_8h_html_acd6eb423f54dce8544f7c3b1618c0374"></a>
<a id="aztest__assert_8h_html_ada3b1fcfa71db1bf7787c03ff45256d5"></a>

```c
/*
 * Copyright (c) 2016 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_TESTSUITE_ZTEST_ASSERT_H_
#define ZEPHYR_TESTSUITE_ZTEST_ASSERT_H_

#include <stdarg.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>

#include <zephyr/sys/util.h>
#include <zephyr/tc_util.h>
#include <zephyr/ztest.h>

#if defined(__cplusplus) && (__cplusplus >= 201103L)
/* Raw pointers; arrays and functions decay during template deduction. */
template < typename T >
static inline bool z_ztest_is_null(T *ptr)
{
        return ptr == nullptr;
}
/* Anything else comparable against nullptr, such as smart pointers. */
template < typename T >
static inline auto z_ztest_is_null(const T &ptr) -> decltype(ptr == nullptr)
{
        return ptr == nullptr;
}
static inline bool z_ztest_is_null(decltype(nullptr))
{
        return true;
}
#define Z_ZTEST_IS_NULL(ptr) z_ztest_is_null(ptr)
#else
#define Z_ZTEST_IS_NULL(ptr) is_null_no_warn((void *)(ptr))
#endif

#ifdef __cplusplus
extern "C" {
#endif

const char *ztest_relative_filename(const char *file);
void ztest_test_fail(void);
void ztest_test_skip(void);
void ztest_test_expect_fail(void);
void ztest_skip_failed_assumption(void);
#if CONFIG_ZTEST_ASSERT_VERBOSE == 0

static inline bool z_zassert_(bool cond, const char *file, int line)
{
        if (cond == false) {
                PRINT_DATA("\n    Assertion failed at %s:%d\n", ztest_relative_filename(file),
                           line);
                ztest_test_fail();
                return false;
        }

        return true;
}

#define z_zassert(cond, default_msg, file, line, func, msg, ...) z_zassert_(cond, file, line)

static inline bool z_zassume_(bool cond, const char *file, int line)
{
        if (cond == false) {
                PRINT_DATA("\n    Assumption failed at %s:%d\n", ztest_relative_filename(file),
                           line);
                ztest_skip_failed_assumption();
                return false;
        }

        return true;
}

#define z_zassume(cond, default_msg, file, line, func, msg, ...) z_zassume_(cond, file, line)

static inline bool z_zexpect_(bool cond, const char *file, int line)
{
        if (cond == false) {
                PRINT_DATA("\n    Expectation failed at %s:%d\n", ztest_relative_filename(file),
                           line);
                ztest_test_expect_fail();
                return false;
        }

        return true;
}

#define z_zexpect(cond, default_msg, file, line, func, msg, ...) z_zexpect_(cond, file, line)

#else /* CONFIG_ZTEST_ASSERT_VERBOSE != 0 */

static inline __printf_like(6, 7) bool z_zassert(bool cond, const char *default_msg,
                                                 const char *file, int line, const char *func,
                                                 const char *msg, ...)
{
        if (cond == false) {
                va_list vargs;

                va_start(vargs, msg);
                PRINT_DATA("\n    Assertion failed at %s:%d: %s: %s\n",
                           ztest_relative_filename(file), line, func, default_msg);
                vprintk(msg, vargs);
                printk("\n");
                va_end(vargs);
                ztest_test_fail();
                return false;
        }
#if CONFIG_ZTEST_ASSERT_VERBOSE == 2
        else {
                PRINT_DATA("\n   Assertion succeeded at %s:%d (%s)\n",
                           ztest_relative_filename(file), line, func);
        }
#endif
        return true;
}

static inline __printf_like(6, 7) bool z_zassume(bool cond, const char *default_msg,
                                                 const char *file, int line, const char *func,
                                                 const char *msg, ...)
{
        if (cond == false) {
                va_list vargs;

                va_start(vargs, msg);
                PRINT_DATA("\n    Assumption failed at %s:%d: %s: %s\n",
                           ztest_relative_filename(file), line, func, default_msg);
                vprintk(msg, vargs);
                printk("\n");
                va_end(vargs);
                ztest_skip_failed_assumption();
                return false;
        }
#if CONFIG_ZTEST_ASSERT_VERBOSE == 2
        else {
                PRINT_DATA("\n   Assumption succeeded at %s:%d (%s)\n",
                           ztest_relative_filename(file), line, func);
        }
#endif
        return true;
}

static inline __printf_like(6, 7) bool z_zexpect(bool cond, const char *default_msg,
                                                 const char *file, int line, const char *func,
                                                 const char *msg, ...)
{
        if (cond == false) {
                va_list vargs;

                va_start(vargs, msg);
                PRINT_DATA("\n    Expectation failed at %s:%d: %s: %s\n",
                           ztest_relative_filename(file), line, func, default_msg);
                vprintk(msg, vargs);
                printk("\n");
                va_end(vargs);
                ztest_test_expect_fail();
                return false;
        }
#if CONFIG_ZTEST_ASSERT_VERBOSE == 2
        else {
                PRINT_DATA("\n   Expectation succeeded at %s:%d (%s)\n",
                           ztest_relative_filename(file), line, func);
        }
#endif
        return true;
}

#endif /* CONFIG_ZTEST_ASSERT_VERBOSE */


#define _zassert_base(cond, default_msg, msg, ...)                                                 \
        do {                                                                                       \
                bool _msg = (msg != NULL);                                                         \
                bool _ret =                                                                        \
                        z_zassert(cond, _msg ? ("(" default_msg ")") : (default_msg), __FILE__,    \
                                  __LINE__, __func__, _msg ? msg : "", ##__VA_ARGS__);             \
                (void)_msg;                                                                        \
                if (!_ret) {                                                                       \
                        /* If not multithreading, return from the test function. */                \
                        COND_CODE_1(CONFIG_MULTITHREADING, (), (return;))                          \
                }                                                                                  \
        } while (0)

#define _zassert_va(cond, default_msg, msg, ...)                                                   \
        _zassert_base(cond, default_msg, msg, ##__VA_ARGS__)

#define zassert(cond, default_msg, ...)                                                            \
        _zassert_va(cond, default_msg, COND_CODE_1(__VA_OPT__(1), (__VA_ARGS__), (NULL)))

#define _zassume_base(cond, default_msg, msg, ...)                                                 \
        do {                                                                                       \
                bool _msg = (msg != NULL);                                                         \
                bool _ret =                                                                        \
                        z_zassume(cond, _msg ? ("(" default_msg ")") : (default_msg), __FILE__,    \
                                  __LINE__, __func__, _msg ? msg : "", ##__VA_ARGS__);             \
                (void)_msg;                                                                        \
                if (!_ret) {                                                                       \
                        /* If not multithreading, return from the test function. */                \
                        COND_CODE_1(CONFIG_MULTITHREADING, (), (return;))                          \
                }                                                                                  \
        } while (0)

#define _zassume_va(cond, default_msg, msg, ...)                                                   \
        _zassume_base(cond, default_msg, msg, ##__VA_ARGS__)

#define zassume(cond, default_msg, ...)                                                            \
        _zassume_va(cond, default_msg, COND_CODE_1(__VA_OPT__(1), (__VA_ARGS__), (NULL)))

#define _zexpect_base(cond, default_msg, msg, ...)                                                 \
        do {                                                                                       \
                bool _msg = (msg != NULL);                                                         \
                bool _ret =                                                                        \
                        z_zexpect(cond, _msg ? ("(" default_msg ")") : (default_msg), __FILE__,    \
                                  __LINE__, __func__, _msg ? msg : "", ##__VA_ARGS__);             \
                (void)_msg;                                                                        \
                if (!_ret) {                                                                       \
                        /* If not multithreading, return from the test function. */                \
                        COND_CODE_1(CONFIG_MULTITHREADING, (), (return;))                          \
                }                                                                                  \
        } while (0)

#define _zexpect_va(cond, default_msg, msg, ...)                                                   \
        _zexpect_base(cond, default_msg, msg, ##__VA_ARGS__)

#define zexpect(cond, default_msg, ...)                                                            \
        _zexpect_va(cond, default_msg, COND_CODE_1(__VA_OPT__(1), (__VA_ARGS__), (NULL)))

#define zassert_unreachable(...) zassert(0, "Reached unreachable code", ##__VA_ARGS__)

#define zassert_true(cond, ...) zassert(cond, #cond " is false", ##__VA_ARGS__)

#define zassert_false(cond, ...) zassert(!(cond), #cond " is true", ##__VA_ARGS__)

#define zassert_ok(cond, ...) zassert((cond) == 0, #cond " is non-zero", ##__VA_ARGS__)

#define zassert_not_ok(cond, ...) zassert((cond) != 0, #cond " is zero", ##__VA_ARGS__)

#define zassert_is_null(ptr, ...)                                                                  \
        zassert(Z_ZTEST_IS_NULL(ptr), #ptr " is not NULL", ##__VA_ARGS__)

#define zassert_not_null(ptr, ...)                                                                 \
        zassert(!Z_ZTEST_IS_NULL(ptr), #ptr " is NULL", ##__VA_ARGS__)

#define zassert_equal(a, b, ...) zassert((a) == (b), #a " not equal to " #b, ##__VA_ARGS__)

#define zassert_not_equal(a, b, ...) zassert((a) != (b), #a " equal to " #b, ##__VA_ARGS__)

#define zassert_equal_ptr(a, b, ...)                                                               \
        zassert((void *)(a) == (void *)(b), #a " not equal to " #b, ##__VA_ARGS__)

#define zassert_within(a, b, d, ...)                                                               \
        zassert(((a) >= ((b) - (d))) && ((a) <= ((b) + (d))), #a " not within " #b " +/- " #d,     \
                ##__VA_ARGS__)

#define zassert_between_inclusive(a, l, u, ...)                                                    \
        zassert(((a) >= (l)) && ((a) <= (u)), #a " not between " #l " and " #u " inclusive",       \
                ##__VA_ARGS__)

#define zassert_mem_equal(...) zassert_mem_equal__(__VA_ARGS__)

#define zassert_mem_equal__(buf, exp, size, ...)                                                   \
        zassert(memcmp(buf, exp, size) == 0, #buf " not equal to " #exp, ##__VA_ARGS__)

#define zassert_str_equal(s1, s2, ...)                                                             \
        zassert(strcmp(s1, s2) == 0, #s1 " not equal to " #s2, ##__VA_ARGS__)



#define zassume_true(cond, ...) zassume(cond, #cond " is false", ##__VA_ARGS__)

#define zassume_false(cond, ...) zassume(!(cond), #cond " is true", ##__VA_ARGS__)

#define zassume_ok(cond, ...) zassume((cond) == 0, #cond " is non-zero", ##__VA_ARGS__)

#define zassume_not_ok(cond, ...) zassume((cond) != 0, #cond " is zero", ##__VA_ARGS__)

#define zassume_is_null(ptr, ...)                                                                  \
        zassume(Z_ZTEST_IS_NULL(ptr), #ptr " is not NULL", ##__VA_ARGS__)

#define zassume_not_null(ptr, ...)                                                                 \
        zassume(!Z_ZTEST_IS_NULL(ptr), #ptr " is NULL", ##__VA_ARGS__)

#define zassume_equal(a, b, ...) zassume((a) == (b), #a " not equal to " #b, ##__VA_ARGS__)

#define zassume_not_equal(a, b, ...) zassume((a) != (b), #a " equal to " #b, ##__VA_ARGS__)

#define zassume_equal_ptr(a, b, ...)                                                               \
        zassume((void *)(a) == (void *)(b), #a " not equal to " #b, ##__VA_ARGS__)

#define zassume_within(a, b, d, ...)                                                               \
        zassume(((a) >= ((b) - (d))) && ((a) <= ((b) + (d))), #a " not within " #b " +/- " #d,     \
                ##__VA_ARGS__)

#define zassume_between_inclusive(a, l, u, ...)                                                    \
        zassume(((a) >= (l)) && ((a) <= (u)), #a " not between " #l " and " #u " inclusive",       \
                ##__VA_ARGS__)

#define zassume_mem_equal(...) zassume_mem_equal__(__VA_ARGS__)

#define zassume_mem_equal__(buf, exp, size, ...)                                                   \
        zassume(memcmp(buf, exp, size) == 0, #buf " not equal to " #exp, ##__VA_ARGS__)

#define zassume_str_equal(s1, s2, ...)                                                             \
        zassume(strcmp(s1, s2) == 0, #s1 " not equal to " #s2, ##__VA_ARGS__)



#define zexpect_true(cond, ...) zexpect(cond, #cond " is false", ##__VA_ARGS__)

#define zexpect_false(cond, ...) zexpect(!(cond), #cond " is true", ##__VA_ARGS__)

#define zexpect_ok(cond, ...) zexpect((cond) == 0, #cond " is non-zero", ##__VA_ARGS__)

#define zexpect_not_ok(cond, ...) zexpect((cond) != 0, #cond " is zero", ##__VA_ARGS__)

#define zexpect_is_null(ptr, ...)                                                                  \
        zexpect(Z_ZTEST_IS_NULL(ptr), #ptr " is not NULL", ##__VA_ARGS__)

#define zexpect_not_null(ptr, ...)                                                                 \
        zexpect(!Z_ZTEST_IS_NULL(ptr), #ptr " is NULL", ##__VA_ARGS__)

#define zexpect_equal(a, b, ...) zexpect((a) == (b), #a " not equal to " #b, ##__VA_ARGS__)

#define zexpect_not_equal(a, b, ...) zexpect((a) != (b), #a " equal to " #b, ##__VA_ARGS__)

#define zexpect_equal_ptr(a, b, ...)                                                               \
        zexpect((void *)(a) == (void *)(b), #a " not equal to " #b, ##__VA_ARGS__)

#define zexpect_within(a, b, delta, ...)                                                           \
        zexpect(((a) >= ((b) - (delta))) && ((a) <= ((b) + (delta))),                              \
                #a " not within " #b " +/- " #delta, ##__VA_ARGS__)

#define zexpect_between_inclusive(a, lower, upper, ...)                                            \
        zexpect(((a) >= (lower)) && ((a) <= (upper)),                                              \
                #a " not between " #lower " and " #upper " inclusive", ##__VA_ARGS__)

#define zexpect_mem_equal(buf, exp, size, ...)                                                     \
        zexpect(memcmp(buf, exp, size) == 0, #buf " not equal to " #exp, ##__VA_ARGS__)

#define zexpect_str_equal(s1, s2, ...)                                                             \
        zexpect(strcmp(s1, s2) == 0, #s1 " not equal to " #s2, ##__VA_ARGS__)


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_TESTSUITE_ZTEST_ASSERT_H_ */
```

## 57.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2016 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 26 行

原始指针（Raw Pointers）；数组和函数在模板推导（Template Deduction）期间会退化（Decay）为指针。

### 注释 3：原第 32 行

其他可与 `nullptr` 比较的类型，例如智能指针（Smart Pointers）。

### 注释 4：原第 100 行

条件编译（Conditional Compilation）：`CONFIG_ZTEST_ASSERT_VERBOSE != 0`。

### 注释 5：原第 177 行

条件编译配置（Configuration）标记：`CONFIG_ZTEST_ASSERT_VERBOSE`。

### 注释 6：原第 210 行

若未启用多线程（Multithreading），则从测试函数（Test Function）返回。

### 注释 7：原第 247 行

若未启用多线程（Multithreading），则从测试函数（Test Function）返回。

### 注释 8：原第 276 行

若未启用多线程（Multithreading），则从测试函数（Test Function）返回。

### 注释 9：原第 768 行

头文件保护宏（Header guard）标记：`ZEPHYR_TESTSUITE_ZTEST_ASSERT_H_`。

## 57.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ztest__assert_8h.html)
- [stdbool.h](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md)
- [stdio.h](../api_file_reference/P409_____w__zephyr__zephyr__lib__libc__minimal__include__stdio.h_文件参考.md)
- [string.h](../api_file_reference/P472_____w__zephyr__zephyr__lib__libc__minimal__include__string.h_文件参考.md)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [zephyr/tc_util.h](https://docs.zephyrproject.org/latest/doxygen/html/tc__util_8h.html)
- [zephyr/ztest.h](../api_file_reference/P517_____w__zephyr__zephyr__subsys__testsuite__ztest__include__zephyr__ztest.h_文件参考.md)
- [ztest_relative_filename](https://docs.zephyrproject.org/latest/doxygen/html/ztest__assert_8h.html#a06a081e3d716be7e024973cbf305c14b)
- [ztest_test_fail](https://docs.zephyrproject.org/latest/doxygen/html/ztest__assert_8h.html#acd6eb423f54dce8544f7c3b1618c0374)
- [ztest_test_skip](https://docs.zephyrproject.org/latest/doxygen/html/ztest__assert_8h.html#ada3b1fcfa71db1bf7787c03ff45256d5)
- [ztest_test_expect_fail](https://docs.zephyrproject.org/latest/doxygen/html/ztest__assert_8h.html#a5c6bb493c88f7426a827889526dc0772)
- [ztest_skip_failed_assumption](https://docs.zephyrproject.org/latest/doxygen/html/ztest__assert_8h.html#a17537c79021fbc12e56b72ccec4b99c5)
- [PRINT_DATA](https://docs.zephyrproject.org/latest/doxygen/html/tc__util_8h.html#aec98e66470b575771ed484118095b692)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [vprintk](https://docs.zephyrproject.org/latest/doxygen/html/printk_8h.html#a9b5fa01884b98d143218af0cd0ffe841)
- [printk](https://docs.zephyrproject.org/latest/doxygen/html/printk_8h.html#a1bce54a738ce2d9dd6d95ee842ec237c)
- [util.h](../util_reference/P002_通用工具头文件参考.md)
- [tc_util.h](https://docs.zephyrproject.org/latest/doxygen/html/tc__util_8h.html)
- [ztest.h](../api_file_reference/P517_____w__zephyr__zephyr__subsys__testsuite__ztest__include__zephyr__ztest.h_文件参考.md)

---

[上一章](P056_winstream.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P058_ztest_test.h_源码浏览.md)
