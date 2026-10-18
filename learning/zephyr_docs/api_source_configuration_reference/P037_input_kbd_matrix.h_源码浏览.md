---
id: learning.zephyr-docs.api-source-configuration-reference.page-37
title: input_kbd_matrix.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/input__kbd__matrix_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第37章\_input\_kbd\_matrix.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/input__kbd__matrix_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/input__kbd__matrix_8h.html)。

## 37.1\_原始可见代码（Source Code）

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
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00038"></a>
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
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="foldopen00080"></a>
<a id="l00080"></a>
<a id="l00091"></a>
<a id="l00097"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="foldopen00116"></a>
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
<a id="foldopen00137"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="foldopen00145"></a>
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
<a id="foldopen00164"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="foldopen00176"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="foldopen00184"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="foldopen00195"></a>
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
<a id="foldopen00225"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="foldopen00238"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="foldopen00247"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="foldopen00255"></a>
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
<a id="foldopen00277"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="l00334"></a>
<a id="l00343"></a>
<a id="l00344"></a>
<a id="l00355"></a>
<a id="l00356"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="l00371"></a>
<a id="l00372"></a>
<a id="aatomic_8h_html"></a>
<a id="aclock_8h_html"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__atomic__apis_html_ga124f07c3a788e53c3a40e4e1c06d8af8"></a>
<a id="agroup__input__kbd__matrix_html_ga45a596e00af6ebf547f44a01cd07d539"></a>
<a id="agroup__input__kbd__matrix_html_ga6d843c7213bf5c0af9003c165a5f3e03"></a>
<a id="agroup__input__kbd__matrix_html_ga80a384d2041dcee27d7940a1e408d82a"></a>
<a id="agroup__input__kbd__matrix_html_ga8e72535859abe307b4409dc4177b5721"></a>
<a id="agroup__input__kbd__matrix_html_ga90ec50249d8e561d69f550fcaa6bd969"></a>
<a id="agroup__input__kbd__matrix_html_ga938dc38da7e81e5a68b8b9dc585c4bab"></a>
<a id="agroup__input__kbd__matrix_html_gab35f4bf523760933294242ccc8226490"></a>
<a id="agroup__input__kbd__matrix_html_gac7d5c811da0c9ab2660be3c3f2fcfe86"></a>
<a id="agroup__input__kbd__matrix_html_gaec0209680e18da8584bdf41e5229aaae"></a>
<a id="agroup__input__kbd__matrix_html_gaf97b6ff410631f111d7c3a7aa7f64171"></a>
<a id="agroup__subsys__pm__device_html_gaee5546eacb9be7caa9d59ab63926cc4c"></a>
<a id="akernel_8h_html"></a>
<a id="apm_2device_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructinput__kbd__matrix__api_html"></a>
<a id="astructinput__kbd__matrix__api_html_aaae2b1eb357fb4b7f1881ef496d79560"></a>
<a id="astructinput__kbd__matrix__api_html_af04e3f78fde3297a70a63c8a8addb477"></a>
<a id="astructinput__kbd__matrix__api_html_af8211d738527ac44876dd07869862f20"></a>
<a id="astructinput__kbd__matrix__common__config_html"></a>
<a id="astructinput__kbd__matrix__common__config_html_a004cb35eede1e58b27730a46155540e9"></a>
<a id="astructinput__kbd__matrix__common__config_html_a0fbc6d10c2f15f3a0126e0c229ec9686"></a>
<a id="astructinput__kbd__matrix__common__config_html_a13374b57becd9314ea726ae888f1702a"></a>
<a id="astructinput__kbd__matrix__common__config_html_a2377a3c7cbd195bb6da3d4dfaf1f5972"></a>
<a id="astructinput__kbd__matrix__common__config_html_a34ce838e3ed4a5cb19c8ce961a9da947"></a>
<a id="astructinput__kbd__matrix__common__config_html_a361fd7c63b2ca643e4b957a6c1c85ae4"></a>
<a id="astructinput__kbd__matrix__common__config_html_a47d4177495c1e17b76c1f616720a3aa6"></a>
<a id="astructinput__kbd__matrix__common__config_html_a545fba8a03ced44a95d7bb7f345d763f"></a>
<a id="astructinput__kbd__matrix__common__config_html_a5da560d28d8bfc527d60c10e4aa29ffb"></a>
<a id="astructinput__kbd__matrix__common__config_html_a81ccf8e0a1f49361f55737e0149bd656"></a>
<a id="astructinput__kbd__matrix__common__config_html_aafb384043bed6593b696e11fd34e0f97"></a>
<a id="astructinput__kbd__matrix__common__config_html_ac2343c08359099f383f154655b371cf6"></a>
<a id="astructinput__kbd__matrix__common__config_html_ac67c028c2cf743c1854dc83aed8f4db4"></a>
<a id="astructinput__kbd__matrix__common__config_html_ace0bafa079826819b7df7950cb3e8212"></a>
<a id="astructinput__kbd__matrix__common__config_html_adfb2b978f1d41bdff28acca17cc4ed3d"></a>
<a id="astructinput__kbd__matrix__common__config_html_af3c4f2bcddf50dc2dbf0ad0e54230565"></a>
<a id="astructinput__kbd__matrix__common__data_html"></a>
<a id="astructinput__kbd__matrix__common__data_html_a526586907a6f0e4d1316c4304adda336"></a>
<a id="astructinput__kbd__matrix__common__data_html_a53b66dca86734fa149b672583455bc61"></a>
<a id="astructinput__kbd__matrix__common__data_html_ac54780c609eb2abc67e468470ac3ef83"></a>
<a id="astructinput__kbd__matrix__common__data_html_ac66f323c17cd346bb1b0b0aa8fc2965a"></a>
<a id="astructinput__kbd__matrix__common__data_html_afe0d57cf725c825097ba26b81bd2640c"></a>
<a id="astructk__sem_html"></a>
<a id="astructk__thread_html"></a>
<a id="asys_2util_8h_html"></a>
<a id="atoolchain_8h_html"></a>

```c
/*
 * Copyright 2023 Google LLC
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_INPUT_INPUT_KBD_MATRIX_H_
#define ZEPHYR_INCLUDE_INPUT_INPUT_KBD_MATRIX_H_


#include <zephyr/device.h>
#include <zephyr/kernel.h>
#include <zephyr/pm/device.h>
#include <zephyr/sys/atomic.h>
#include <zephyr/sys/util.h>
#include <zephyr/sys/clock.h>
#include <zephyr/toolchain.h>

#define INPUT_KBD_MATRIX_COLUMN_DRIVE_NONE -1

#define INPUT_KBD_MATRIX_COLUMN_DRIVE_ALL  -2

#define INPUT_KBD_MATRIX_SCAN_OCURRENCES 30U

#if CONFIG_INPUT_KBD_MATRIX_16_BIT_ROW
typedef uint16_t kbd_row_t;
#define PRIkbdrow "04" PRIx16
#else
typedef uint8_t kbd_row_t;
#define PRIkbdrow "02" PRIx8
#endif

#if defined(CONFIG_INPUT_KBD_ACTUAL_KEY_MASK_DYNAMIC) || defined(__DOXYGEN__)
#define INPUT_KBD_ACTUAL_KEY_MASK_CONST
int input_kbd_matrix_actual_key_mask_set(const struct device *dev,
                                          uint8_t row, uint8_t col, bool enabled);
#else
#define INPUT_KBD_ACTUAL_KEY_MASK_CONST const
#endif

#define INPUT_KBD_MATRIX_ROW_BITS NUM_BITS(kbd_row_t)

struct input_kbd_matrix_api {
        void (*drive_column)(const struct device *dev, int col);
        kbd_row_t (*read_row)(const struct device *dev);
        void (*set_detect_mode)(const struct device *dev, bool enabled);
};

struct input_kbd_matrix_common_config {
        const struct input_kbd_matrix_api *api;
        uint8_t row_size;
        uint8_t col_size;
        uint32_t poll_period_us;
        uint32_t stable_poll_period_us;
        uint32_t poll_timeout_ms;
        uint32_t debounce_down_us;
        uint32_t debounce_up_us;
        uint32_t settle_time_us;
        bool ghostkey_check;
        INPUT_KBD_ACTUAL_KEY_MASK_CONST kbd_row_t *actual_key_mask;

        /* extra data pointers */
        kbd_row_t *matrix_stable_state;
        kbd_row_t *matrix_unstable_state;
        kbd_row_t *matrix_previous_state;
        kbd_row_t *matrix_new_state;
        uint8_t *scan_cycle_idx;
};

#define INPUT_KBD_MATRIX_DATA_NAME(node_id, name) \
        _CONCAT(__input_kbd_matrix_, \
                _CONCAT(name, DEVICE_DT_NAME_GET(node_id)))

#define INPUT_KBD_MATRIX_DT_DEFINE_ROW_COL(node_id, _row_size, _col_size) \
        BUILD_ASSERT(IN_RANGE(_row_size, 1, INPUT_KBD_MATRIX_ROW_BITS), "invalid row-size"); \
        BUILD_ASSERT(IN_RANGE(_col_size, 1, UINT8_MAX), "invalid col-size"); \
        IF_ENABLED(DT_NODE_HAS_PROP(node_id, actual_key_mask), ( \
        BUILD_ASSERT(DT_PROP_LEN(node_id, actual_key_mask) == _col_size, \
                     "actual-key-mask size does not match the number of columns"); \
        static INPUT_KBD_ACTUAL_KEY_MASK_CONST kbd_row_t \
                INPUT_KBD_MATRIX_DATA_NAME(node_id, actual_key_mask)[_col_size] = \
                        DT_PROP(node_id, actual_key_mask); \
        )) \
        static kbd_row_t INPUT_KBD_MATRIX_DATA_NAME(node_id, stable_state)[_col_size]; \
        static kbd_row_t INPUT_KBD_MATRIX_DATA_NAME(node_id, unstable_state)[_col_size]; \
        static kbd_row_t INPUT_KBD_MATRIX_DATA_NAME(node_id, previous_state)[_col_size]; \
        static kbd_row_t INPUT_KBD_MATRIX_DATA_NAME(node_id, new_state)[_col_size]; \
        static uint8_t INPUT_KBD_MATRIX_DATA_NAME(node_id, scan_cycle_idx)[_row_size * _col_size];

#define INPUT_KBD_MATRIX_DT_DEFINE(node_id) \
        INPUT_KBD_MATRIX_DT_DEFINE_ROW_COL( \
                node_id, DT_PROP(node_id, row_size), DT_PROP(node_id, col_size))

#define INPUT_KBD_MATRIX_DT_INST_DEFINE_ROW_COL(inst, row_size, col_size) \
        INPUT_KBD_MATRIX_DT_DEFINE_ROW_COL(DT_DRV_INST(inst), row_size, col_size)

#define INPUT_KBD_MATRIX_DT_INST_DEFINE(inst) \
        INPUT_KBD_MATRIX_DT_DEFINE(DT_DRV_INST(inst))

#define INPUT_KBD_MATRIX_DT_COMMON_CONFIG_INIT_ROW_COL(node_id, _api, _row_size, _col_size) \
        { \
                .api = _api, \
                .row_size = _row_size, \
                .col_size = _col_size, \
                .poll_period_us = DT_PROP(node_id, poll_period_us), \
                .stable_poll_period_us = DT_PROP_OR(node_id, stable_poll_period_us, \
                                                    DT_PROP(node_id, poll_period_us)), \
                .poll_timeout_ms = DT_PROP(node_id, poll_timeout_ms), \
                .debounce_down_us = DT_PROP(node_id, debounce_down_ms) * USEC_PER_MSEC, \
                .debounce_up_us = DT_PROP(node_id, debounce_up_ms) * USEC_PER_MSEC, \
                .settle_time_us = DT_PROP(node_id, settle_time_us), \
                .ghostkey_check = !DT_PROP(node_id, no_ghostkey_check), \
                IF_ENABLED(DT_NODE_HAS_PROP(node_id, actual_key_mask), ( \
                .actual_key_mask = INPUT_KBD_MATRIX_DATA_NAME(node_id, actual_key_mask), \
                )) \
                \
                .matrix_stable_state = INPUT_KBD_MATRIX_DATA_NAME(node_id, stable_state), \
                .matrix_unstable_state = INPUT_KBD_MATRIX_DATA_NAME(node_id, unstable_state), \
                .matrix_previous_state = INPUT_KBD_MATRIX_DATA_NAME(node_id, previous_state), \
                .matrix_new_state = INPUT_KBD_MATRIX_DATA_NAME(node_id, new_state), \
                .scan_cycle_idx = INPUT_KBD_MATRIX_DATA_NAME(node_id, scan_cycle_idx), \
        }

#define INPUT_KBD_MATRIX_DT_COMMON_CONFIG_INIT(node_id, api) \
        INPUT_KBD_MATRIX_DT_COMMON_CONFIG_INIT_ROW_COL( \
                node_id, api, DT_PROP(node_id, row_size), DT_PROP(node_id, col_size))

#define INPUT_KBD_MATRIX_DT_INST_COMMON_CONFIG_INIT_ROW_COL(inst, api, row_size, col_size) \
        INPUT_KBD_MATRIX_DT_COMMON_CONFIG_INIT_ROW_COL(DT_DRV_INST(inst), api, row_size, col_size)

#define INPUT_KBD_MATRIX_DT_INST_COMMON_CONFIG_INIT(inst, api) \
        INPUT_KBD_MATRIX_DT_COMMON_CONFIG_INIT(DT_DRV_INST(inst), api)

struct input_kbd_matrix_common_data {
        /* Track previous cycles, used for debouncing. */
        uint32_t scan_clk_cycle[INPUT_KBD_MATRIX_SCAN_OCURRENCES];
        uint8_t scan_cycles_idx;

        struct k_sem poll_lock;
#ifdef CONFIG_PM_DEVICE
        atomic_t suspended;
#endif

        struct k_thread thread;

        K_KERNEL_STACK_MEMBER(thread_stack,
                              CONFIG_INPUT_KBD_MATRIX_THREAD_STACK_SIZE);
};

#define INPUT_KBD_STRUCT_CHECK(config, data) \
        BUILD_ASSERT(offsetof(config, common) == 0, \
                     "struct input_kbd_matrix_common_config must be placed first"); \
        BUILD_ASSERT(offsetof(data, common) == 0, \
                     "struct input_kbd_matrix_common_data must be placed first")

void input_kbd_matrix_poll_start(const struct device *dev);

#if defined(CONFIG_INPUT_KBD_DRIVE_COLUMN_HOOK) || defined(__DOXYGEN__)
void input_kbd_matrix_drive_column_hook(const struct device *dev, int col);
#endif

int input_kbd_matrix_common_init(const struct device *dev);

#ifdef CONFIG_PM_DEVICE
int input_kbd_matrix_pm_action(const struct device *dev,
                               enum pm_device_action action);
#endif

bool input_kbd_matrix_ghosting(const struct device *dev);

void input_kbd_matrix_update_state(const struct device *dev);

bool input_kbd_matrix_active(const struct device *dev);


#endif /* ZEPHYR_INCLUDE_INPUT_INPUT_KBD_MATRIX_H_ */
```

## 37.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2023 Google LLC。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 129 行

附加数据指针（Extra data pointers）。

### 注释 3：原第 256 行

跟踪先前的周期值，用于消抖（Debouncing）。

### 注释 4：原第 372 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_INPUT_INPUT_KBD_MATRIX_H_`。

## 37.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/input__kbd__matrix_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/pm/device.h](../power/P069_设备电源管理头文件.md)
- [zephyr/sys/atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [zephyr/sys/clock.h](../timer_reference/P090_系统时钟头文件参考.md)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [kbd_row_t](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#gac7d5c811da0c9ab2660be3c3f2fcfe86)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [input_kbd_matrix_actual_key_mask_set](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#gab35f4bf523760933294242ccc8226490)
- [device](../device_reference/P002_设备对象结构.md)
- [input_kbd_matrix_api](../system_service_model_reference/P054_input_kbd_matrix_api_结构体.md)
- [drive_column](../system_service_model_reference/P054_input_kbd_matrix_api_结构体.md#af8211d738527ac44876dd07869862f20)
- [read_row](../system_service_model_reference/P054_input_kbd_matrix_api_结构体.md#af04e3f78fde3297a70a63c8a8addb477)
- [set_detect_mode](../system_service_model_reference/P054_input_kbd_matrix_api_结构体.md#aaae2b1eb357fb4b7f1881ef496d79560)
- [input_kbd_matrix_common_config](../system_service_model_reference/P055_input_kbd_matrix_common_config_结构体.md)
- [api](../system_service_model_reference/P055_input_kbd_matrix_common_config_结构体.md#ace0bafa079826819b7df7950cb3e8212)
- [row_size](../system_service_model_reference/P055_input_kbd_matrix_common_config_结构体.md#af3c4f2bcddf50dc2dbf0ad0e54230565)
- [col_size](../system_service_model_reference/P055_input_kbd_matrix_common_config_结构体.md#adfb2b978f1d41bdff28acca17cc4ed3d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [poll_period_us](../system_service_model_reference/P055_input_kbd_matrix_common_config_结构体.md#a34ce838e3ed4a5cb19c8ce961a9da947)
- [stable_poll_period_us](../system_service_model_reference/P055_input_kbd_matrix_common_config_结构体.md#ac67c028c2cf743c1854dc83aed8f4db4)
- [poll_timeout_ms](../system_service_model_reference/P055_input_kbd_matrix_common_config_结构体.md#a81ccf8e0a1f49361f55737e0149bd656)
- [debounce_down_us](../system_service_model_reference/P055_input_kbd_matrix_common_config_结构体.md#a004cb35eede1e58b27730a46155540e9)
- [debounce_up_us](../system_service_model_reference/P055_input_kbd_matrix_common_config_结构体.md#a545fba8a03ced44a95d7bb7f345d763f)
- [settle_time_us](../system_service_model_reference/P055_input_kbd_matrix_common_config_结构体.md#a13374b57becd9314ea726ae888f1702a)
- [ghostkey_check](../system_service_model_reference/P055_input_kbd_matrix_common_config_结构体.md#a2377a3c7cbd195bb6da3d4dfaf1f5972)
- [INPUT_KBD_ACTUAL_KEY_MASK_CONST](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#gaec0209680e18da8584bdf41e5229aaae)
- [actual_key_mask](../system_service_model_reference/P055_input_kbd_matrix_common_config_结构体.md#ac2343c08359099f383f154655b371cf6)
- [matrix_stable_state](../system_service_model_reference/P055_input_kbd_matrix_common_config_结构体.md#aafb384043bed6593b696e11fd34e0f97)
- [matrix_unstable_state](../system_service_model_reference/P055_input_kbd_matrix_common_config_结构体.md#a47d4177495c1e17b76c1f616720a3aa6)
- [matrix_previous_state](../system_service_model_reference/P055_input_kbd_matrix_common_config_结构体.md#a361fd7c63b2ca643e4b957a6c1c85ae4)
- [matrix_new_state](../system_service_model_reference/P055_input_kbd_matrix_common_config_结构体.md#a5da560d28d8bfc527d60c10e4aa29ffb)
- [scan_cycle_idx](../system_service_model_reference/P055_input_kbd_matrix_common_config_结构体.md#a0fbc6d10c2f15f3a0126e0c229ec9686)
- [input_kbd_matrix_common_data](../system_service_model_reference/P056_input_kbd_matrix_common_data_结构体.md)
- [scan_clk_cycle](../system_service_model_reference/P056_input_kbd_matrix_common_data_结构体.md#ac54780c609eb2abc67e468470ac3ef83)
- [INPUT_KBD_MATRIX_SCAN_OCURRENCES](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#ga80a384d2041dcee27d7940a1e408d82a)
- [scan_cycles_idx](../system_service_model_reference/P056_input_kbd_matrix_common_data_结构体.md#a53b66dca86734fa149b672583455bc61)
- [k_sem](../synchronization_reference/P009_内核信号量结构.md)
- [poll_lock](../system_service_model_reference/P056_input_kbd_matrix_common_data_结构体.md#afe0d57cf725c825097ba26b81bd2640c)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [k_thread](../thread_core_reference/P004_线程对象结构.md)
- [thread](../system_service_model_reference/P056_input_kbd_matrix_common_data_结构体.md#a526586907a6f0e4d1316c4304adda336)
- [K_KERNEL_STACK_MEMBER](../system_service_model_reference/P056_input_kbd_matrix_common_data_结构体.md#ac66f323c17cd346bb1b0b0aa8fc2965a)
- [input_kbd_matrix_poll_start](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#gaf97b6ff410631f111d7c3a7aa7f64171)
- [input_kbd_matrix_drive_column_hook](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#ga6d843c7213bf5c0af9003c165a5f3e03)
- [input_kbd_matrix_common_init](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#ga938dc38da7e81e5a68b8b9dc585c4bab)
- [pm_device_action](https://docs.zephyrproject.org/latest/doxygen/html/group__subsys__pm__device.html#gaee5546eacb9be7caa9d59ab63926cc4c)
- [input_kbd_matrix_ghosting](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#ga8e72535859abe307b4409dc4177b5721)
- [input_kbd_matrix_update_state](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#ga45a596e00af6ebf547f44a01cd07d539)
- [input_kbd_matrix_active](https://docs.zephyrproject.org/latest/doxygen/html/group__input__kbd__matrix.html#ga90ec50249d8e561d69f550fcaa6bd969)
- [atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [clock.h](../timer_reference/P090_系统时钟头文件参考.md)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [device.h](../power/P069_设备电源管理头文件.md)
- [input_kbd_matrix_api::set_detect_mode](../system_service_model_reference/P054_input_kbd_matrix_api_结构体.md#aaae2b1eb357fb4b7f1881ef496d79560)
- [input_kbd_matrix_api::read_row](../system_service_model_reference/P054_input_kbd_matrix_api_结构体.md#af04e3f78fde3297a70a63c8a8addb477)
- [input_kbd_matrix_api::drive_column](../system_service_model_reference/P054_input_kbd_matrix_api_结构体.md#af8211d738527ac44876dd07869862f20)
- [input_kbd_matrix_common_config::debounce_down_us](../system_service_model_reference/P055_input_kbd_matrix_common_config_结构体.md#a004cb35eede1e58b27730a46155540e9)
- [input_kbd_matrix_common_config::scan_cycle_idx](../system_service_model_reference/P055_input_kbd_matrix_common_config_结构体.md#a0fbc6d10c2f15f3a0126e0c229ec9686)
- [input_kbd_matrix_common_config::settle_time_us](../system_service_model_reference/P055_input_kbd_matrix_common_config_结构体.md#a13374b57becd9314ea726ae888f1702a)
- [input_kbd_matrix_common_config::ghostkey_check](../system_service_model_reference/P055_input_kbd_matrix_common_config_结构体.md#a2377a3c7cbd195bb6da3d4dfaf1f5972)
- [input_kbd_matrix_common_config::poll_period_us](../system_service_model_reference/P055_input_kbd_matrix_common_config_结构体.md#a34ce838e3ed4a5cb19c8ce961a9da947)
- [input_kbd_matrix_common_config::matrix_previous_state](../system_service_model_reference/P055_input_kbd_matrix_common_config_结构体.md#a361fd7c63b2ca643e4b957a6c1c85ae4)
- [input_kbd_matrix_common_config::matrix_unstable_state](../system_service_model_reference/P055_input_kbd_matrix_common_config_结构体.md#a47d4177495c1e17b76c1f616720a3aa6)
- [input_kbd_matrix_common_config::debounce_up_us](../system_service_model_reference/P055_input_kbd_matrix_common_config_结构体.md#a545fba8a03ced44a95d7bb7f345d763f)
- [input_kbd_matrix_common_config::matrix_new_state](../system_service_model_reference/P055_input_kbd_matrix_common_config_结构体.md#a5da560d28d8bfc527d60c10e4aa29ffb)
- [input_kbd_matrix_common_config::poll_timeout_ms](../system_service_model_reference/P055_input_kbd_matrix_common_config_结构体.md#a81ccf8e0a1f49361f55737e0149bd656)
- [input_kbd_matrix_common_config::matrix_stable_state](../system_service_model_reference/P055_input_kbd_matrix_common_config_结构体.md#aafb384043bed6593b696e11fd34e0f97)
- [input_kbd_matrix_common_config::actual_key_mask](../system_service_model_reference/P055_input_kbd_matrix_common_config_结构体.md#ac2343c08359099f383f154655b371cf6)
- [input_kbd_matrix_common_config::stable_poll_period_us](../system_service_model_reference/P055_input_kbd_matrix_common_config_结构体.md#ac67c028c2cf743c1854dc83aed8f4db4)
- [input_kbd_matrix_common_config::api](../system_service_model_reference/P055_input_kbd_matrix_common_config_结构体.md#ace0bafa079826819b7df7950cb3e8212)
- [input_kbd_matrix_common_config::col_size](../system_service_model_reference/P055_input_kbd_matrix_common_config_结构体.md#adfb2b978f1d41bdff28acca17cc4ed3d)
- [input_kbd_matrix_common_config::row_size](../system_service_model_reference/P055_input_kbd_matrix_common_config_结构体.md#af3c4f2bcddf50dc2dbf0ad0e54230565)
- [input_kbd_matrix_common_data::thread](../system_service_model_reference/P056_input_kbd_matrix_common_data_结构体.md#a526586907a6f0e4d1316c4304adda336)
- [input_kbd_matrix_common_data::scan_cycles_idx](../system_service_model_reference/P056_input_kbd_matrix_common_data_结构体.md#a53b66dca86734fa149b672583455bc61)
- [input_kbd_matrix_common_data::scan_clk_cycle](../system_service_model_reference/P056_input_kbd_matrix_common_data_结构体.md#ac54780c609eb2abc67e468470ac3ef83)
- [input_kbd_matrix_common_data::K_KERNEL_STACK_MEMBER](../system_service_model_reference/P056_input_kbd_matrix_common_data_结构体.md#ac66f323c17cd346bb1b0b0aa8fc2965a)
- [input_kbd_matrix_common_data::poll_lock](../system_service_model_reference/P056_input_kbd_matrix_common_data_结构体.md#afe0d57cf725c825097ba26b81bd2640c)
- [util.h](../util_reference/P002_通用工具头文件参考.md)
- [toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)

---

[上一章](P036_infineon-xmc4xxx-gpio.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P038_inspect.h_源码浏览.md)
