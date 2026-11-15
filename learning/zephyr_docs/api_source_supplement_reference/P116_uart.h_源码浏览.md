---
id: learning.zephyr-docs.api-source-supplement-reference.page-116
title: uart.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/modem_2backend_2uart_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第116章\_uart.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/modem_2backend_2uart_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/modem_2backend_2uart_8h.html)。

## 116.1\_原始可见代码（Source Code）

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
<a id="foldopen00024"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="foldopen00033"></a>
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
<a id="foldopen00059"></a>
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
<a id="foldopen00069"></a>
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
<a id="foldopen00087"></a>
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
<a id="aatomic_8h_html"></a>
<a id="adevice_8h_html"></a>
<a id="adrivers_2uart_8h_html"></a>
<a id="agroup__atomic__apis_html_ga124f07c3a788e53c3a40e4e1c06d8af8"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="amodem_2backend_2uart_8h_html_a7f7550ddcf3a7ea1493c788b635862ba"></a>
<a id="amodem_2stats_8h_html"></a>
<a id="apipe_8h_html"></a>
<a id="aring__buffer_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructdevice_html"></a>
<a id="astructgpio__dt__spec_html"></a>
<a id="astructk__spinlock_html"></a>
<a id="astructk__work__delayable_html"></a>
<a id="astructk__work_html"></a>
<a id="astructmodem__backend__uart__async__common_html"></a>
<a id="astructmodem__backend__uart__async__common_html_a37c79230e6f796fa12dfc4eed5e94fcc"></a>
<a id="astructmodem__backend__uart__async__common_html_a3996a268ebdeefec160ed80d122ce533"></a>
<a id="astructmodem__backend__uart__async__common_html_a41f85b18c22fc678ce06b5ea42dd052a"></a>
<a id="astructmodem__backend__uart__async__common_html_a4e542d2880b320f3b843fc3813c0fd0f"></a>
<a id="astructmodem__backend__uart__async_html"></a>
<a id="astructmodem__backend__uart__async_html_a85e0e51366bbb2e1d7a72e0b9a0650ee"></a>
<a id="astructmodem__backend__uart__async_html_a8c186bed442db94aa84bf76ad3253fc2"></a>
<a id="astructmodem__backend__uart__async_html_a8e6ff3cae3a79e8b26e67282bb50f5ad"></a>
<a id="astructmodem__backend__uart__async_html_ab61b263cdbe9bfb796f3dd6ed69b3dea"></a>
<a id="astructmodem__backend__uart__async_html_ac3909d735bfecac46001f1b289e222a2"></a>
<a id="astructmodem__backend__uart__config_html"></a>
<a id="astructmodem__backend__uart__config_html_a2576f671e21a1fa75163ac63ac5e56a4"></a>
<a id="astructmodem__backend__uart__config_html_a3dad78dbaddbdc94c57f5381d9a5c68f"></a>
<a id="astructmodem__backend__uart__config_html_a48c4a5e9de64bcb435d9b8aea05bfd87"></a>
<a id="astructmodem__backend__uart__config_html_a4f8752a33e75164370a8eb81615c2555"></a>
<a id="astructmodem__backend__uart__config_html_a64f82b3b4bf6d1ff6081ac075b67a0b0"></a>
<a id="astructmodem__backend__uart__config_html_ad80a5bd5efcf37931503049ac2ba788d"></a>
<a id="astructmodem__backend__uart__isr_html"></a>
<a id="astructmodem__backend__uart__isr_html_a2c50ecd1dad68ee2aa2ad57b1b746831"></a>
<a id="astructmodem__backend__uart__isr_html_a3b0413caf39e82a52e2bbab6ba42ac3b"></a>
<a id="astructmodem__backend__uart__isr_html_a4d270cc8e2260c349c588109a3c4ddae"></a>
<a id="astructmodem__backend__uart__isr_html_a69aa3fbffb2bfbd8d5ca16effb8f4f17"></a>
<a id="astructmodem__backend__uart__isr_html_ac7a373618e4dc5dfda02bbc9d09a11a3"></a>
<a id="astructmodem__backend__uart__isr_html_afacd3e6c890a30188987e6cffae03981"></a>
<a id="astructmodem__backend__uart_html"></a>
<a id="astructmodem__backend__uart_html_a26f3331f0ae7d9384f369ae50694090d"></a>
<a id="astructmodem__backend__uart_html_a369c5fd2072e42f5eedfe03a5d312ec6"></a>
<a id="astructmodem__backend__uart_html_a387327d6378834136fe6a0e80cec7337"></a>
<a id="astructmodem__backend__uart_html_a812165945d6a4aba4fd6bc5ba26b3082"></a>
<a id="astructmodem__backend__uart_html_aafd345ff47cc51a9e1100604a51f6b2d"></a>
<a id="astructmodem__backend__uart_html_abdf5e8696db6f2732359000abbd60dca"></a>
<a id="astructmodem__backend__uart_html_af7e0483a6398b6893ac4693e2bc12f31"></a>
<a id="astructring__buf_html"></a>

```c
/*
 * Copyright (c) 2022 Trackunit Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#include <zephyr/kernel.h>
#include <zephyr/types.h>
#include <zephyr/device.h>
#include <zephyr/drivers/uart.h>
#include <zephyr/sys/ring_buffer.h>
#include <zephyr/sys/atomic.h>

#include <zephyr/modem/pipe.h>
#include <zephyr/modem/stats.h>

#ifndef ZEPHYR_INCLUDE_MODEM_BACKEND_UART_H_
#define ZEPHYR_INCLUDE_MODEM_BACKEND_UART_H_

#ifdef __cplusplus
extern "C" {
#endif

struct modem_backend_uart_isr {
        struct ring_buf receive_rdb[2];
        struct ring_buf transmit_rb;
        atomic_t transmit_buf_len;
        atomic_t receive_buf_len;
        uint8_t receive_rdb_used;
        uint32_t transmit_buf_put_limit;
};

struct modem_backend_uart_async_common {
        uint8_t *transmit_buf;
        uint32_t transmit_buf_size;
        struct k_work rx_disabled_work;
        atomic_t state;
};

#ifdef CONFIG_MODEM_BACKEND_UART_ASYNC_HWFC

struct rx_queue_event {
        uint8_t *buf;
        size_t len;
};

struct modem_backend_uart_async {
        struct modem_backend_uart_async_common common;
        struct k_mem_slab rx_slab;
        struct k_msgq rx_queue;
        struct rx_queue_event rx_event;
        struct rx_queue_event rx_queue_buf[CONFIG_MODEM_BACKEND_UART_ASYNC_HWFC_BUFFER_COUNT];
        uint32_t rx_buf_size;
        uint8_t rx_buf_count;
};

#else

struct modem_backend_uart_async {
        struct modem_backend_uart_async_common common;
        uint8_t *receive_bufs[2];
        uint32_t receive_buf_size;
        struct ring_buf receive_rb;
        struct k_spinlock receive_rb_lock;
};

#endif /* CONFIG_MODEM_BACKEND_UART_ASYNC_HWFC */

struct modem_backend_uart {
        const struct device *uart;
        const struct gpio_dt_spec *dtr_gpio;
        struct modem_pipe pipe;
        struct k_work_delayable receive_ready_work;
        struct k_work transmit_idle_work;

#if CONFIG_MODEM_STATS
        struct modem_stats_buffer receive_buf_stats;
        struct modem_stats_buffer transmit_buf_stats;
#endif

        union {
                struct modem_backend_uart_isr isr;
                struct modem_backend_uart_async async;
        };
};

struct modem_backend_uart_config {
        const struct device *uart;
        const struct gpio_dt_spec *dtr_gpio;
        /* Address must be word-aligned when CONFIG_MODEM_BACKEND_UART_ASYNC_HWFC is enabled. */
        uint8_t *receive_buf;
        uint32_t receive_buf_size;
        uint8_t *transmit_buf;
        uint32_t transmit_buf_size;
};

struct modem_pipe *modem_backend_uart_init(struct modem_backend_uart *backend,
                                           const struct modem_backend_uart_config *config);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_MODEM_BACKEND_UART_H_ */
```

## 116.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Trackunit Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 67 行

条件编译配置（Configuration）标记：`CONFIG_MODEM_BACKEND_UART_ASYNC_HWFC`。

### 注释 3：原第 90 行

启用 `CONFIG_MODEM_BACKEND_UART_ASYNC_HWFC` 时，地址必须按字对齐（Word-aligned）。

### 注释 4：原第 104 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MODEM_BACKEND_UART_H_`。

## 116.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/modem_2backend_2uart_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/drivers/uart.h](../uart_driver_reference/P001_UART驱动头文件参考.md)
- [zephyr/sys/ring_buffer.h](../ringbuffer_reference/P003_环形缓冲区头文件参考.md)
- [zephyr/sys/atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [zephyr/modem/pipe.h](https://docs.zephyrproject.org/latest/doxygen/html/pipe_8h.html)
- [zephyr/modem/stats.h](https://docs.zephyrproject.org/latest/doxygen/html/modem_2stats_8h.html)
- [modem_backend_uart_isr](../modem_wireless_model_reference/P047_modem_backend_uart_isr_结构体.md)
- [ring_buf](../ringbuffer_reference/P002_环形缓冲区结构.md)
- [receive_rdb](../modem_wireless_model_reference/P047_modem_backend_uart_isr_结构体.md#afacd3e6c890a30188987e6cffae03981)
- [transmit_rb](../modem_wireless_model_reference/P047_modem_backend_uart_isr_结构体.md#a69aa3fbffb2bfbd8d5ca16effb8f4f17)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [transmit_buf_len](../modem_wireless_model_reference/P047_modem_backend_uart_isr_结构体.md#a4d270cc8e2260c349c588109a3c4ddae)
- [receive_buf_len](../modem_wireless_model_reference/P047_modem_backend_uart_isr_结构体.md#a2c50ecd1dad68ee2aa2ad57b1b746831)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [receive_rdb_used](../modem_wireless_model_reference/P047_modem_backend_uart_isr_结构体.md#ac7a373618e4dc5dfda02bbc9d09a11a3)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [transmit_buf_put_limit](../modem_wireless_model_reference/P047_modem_backend_uart_isr_结构体.md#a3b0413caf39e82a52e2bbab6ba42ac3b)
- [modem_backend_uart_async_common](../modem_wireless_model_reference/P045_modem_backend_uart_async_common_结构体.md)
- [transmit_buf](../modem_wireless_model_reference/P045_modem_backend_uart_async_common_结构体.md#a41f85b18c22fc678ce06b5ea42dd052a)
- [transmit_buf_size](../modem_wireless_model_reference/P045_modem_backend_uart_async_common_结构体.md#a37c79230e6f796fa12dfc4eed5e94fcc)
- [k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)
- [rx_disabled_work](../modem_wireless_model_reference/P045_modem_backend_uart_async_common_结构体.md#a3996a268ebdeefec160ed80d122ce533)
- [state](../modem_wireless_model_reference/P045_modem_backend_uart_async_common_结构体.md#a4e542d2880b320f3b843fc3813c0fd0f)
- [modem_backend_uart_async](../modem_wireless_model_reference/P044_modem_backend_uart_async_结构体.md)
- [common](../modem_wireless_model_reference/P044_modem_backend_uart_async_结构体.md#a8c186bed442db94aa84bf76ad3253fc2)
- [receive_bufs](../modem_wireless_model_reference/P044_modem_backend_uart_async_结构体.md#a8e6ff3cae3a79e8b26e67282bb50f5ad)
- [receive_buf_size](../modem_wireless_model_reference/P044_modem_backend_uart_async_结构体.md#a85e0e51366bbb2e1d7a72e0b9a0650ee)
- [receive_rb](../modem_wireless_model_reference/P044_modem_backend_uart_async_结构体.md#ac3909d735bfecac46001f1b289e222a2)
- [k_spinlock](../kernel/P066_自旋锁结构参考.md)
- [receive_rb_lock](../modem_wireless_model_reference/P044_modem_backend_uart_async_结构体.md#ab61b263cdbe9bfb796f3dd6ed69b3dea)
- [modem_backend_uart](../modem_wireless_model_reference/P043_modem_backend_uart_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uart](../modem_wireless_model_reference/P043_modem_backend_uart_结构体.md#a26f3331f0ae7d9384f369ae50694090d)
- [gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)
- [dtr_gpio](../modem_wireless_model_reference/P043_modem_backend_uart_结构体.md#abdf5e8696db6f2732359000abbd60dca)
- [pipe](../modem_wireless_model_reference/P043_modem_backend_uart_结构体.md#af7e0483a6398b6893ac4693e2bc12f31)
- [k_work_delayable](../kernel_runtime_model_reference/P009_k_work_delayable_结构体.md)
- [receive_ready_work](../modem_wireless_model_reference/P043_modem_backend_uart_结构体.md#a369c5fd2072e42f5eedfe03a5d312ec6)
- [transmit_idle_work](../modem_wireless_model_reference/P043_modem_backend_uart_结构体.md#aafd345ff47cc51a9e1100604a51f6b2d)
- [isr](../modem_wireless_model_reference/P043_modem_backend_uart_结构体.md#a812165945d6a4aba4fd6bc5ba26b3082)
- [async](../modem_wireless_model_reference/P043_modem_backend_uart_结构体.md#a387327d6378834136fe6a0e80cec7337)
- [modem_backend_uart_config](../modem_wireless_model_reference/P046_modem_backend_uart_config_结构体.md)
- [uart](../modem_wireless_model_reference/P046_modem_backend_uart_config_结构体.md#a4f8752a33e75164370a8eb81615c2555)
- [dtr_gpio](../modem_wireless_model_reference/P046_modem_backend_uart_config_结构体.md#a3dad78dbaddbdc94c57f5381d9a5c68f)
- [receive_buf](../modem_wireless_model_reference/P046_modem_backend_uart_config_结构体.md#ad80a5bd5efcf37931503049ac2ba788d)
- [receive_buf_size](../modem_wireless_model_reference/P046_modem_backend_uart_config_结构体.md#a2576f671e21a1fa75163ac63ac5e56a4)
- [transmit_buf](../modem_wireless_model_reference/P046_modem_backend_uart_config_结构体.md#a64f82b3b4bf6d1ff6081ac075b67a0b0)
- [transmit_buf_size](../modem_wireless_model_reference/P046_modem_backend_uart_config_结构体.md#a48c4a5e9de64bcb435d9b8aea05bfd87)
- [modem_backend_uart_init](https://docs.zephyrproject.org/latest/doxygen/html/modem_2backend_2uart_8h.html#a7f7550ddcf3a7ea1493c788b635862ba)
- [atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [uart.h](../uart_driver_reference/P001_UART驱动头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [stats.h](https://docs.zephyrproject.org/latest/doxygen/html/modem_2stats_8h.html)
- [pipe.h](https://docs.zephyrproject.org/latest/doxygen/html/pipe_8h.html)
- [ring_buffer.h](../ringbuffer_reference/P003_环形缓冲区头文件参考.md)
- [modem_backend_uart_async_common::transmit_buf_size](../modem_wireless_model_reference/P045_modem_backend_uart_async_common_结构体.md#a37c79230e6f796fa12dfc4eed5e94fcc)
- [modem_backend_uart_async_common::rx_disabled_work](../modem_wireless_model_reference/P045_modem_backend_uart_async_common_结构体.md#a3996a268ebdeefec160ed80d122ce533)
- [modem_backend_uart_async_common::transmit_buf](../modem_wireless_model_reference/P045_modem_backend_uart_async_common_结构体.md#a41f85b18c22fc678ce06b5ea42dd052a)
- [modem_backend_uart_async_common::state](../modem_wireless_model_reference/P045_modem_backend_uart_async_common_结构体.md#a4e542d2880b320f3b843fc3813c0fd0f)
- [modem_backend_uart_async::receive_buf_size](../modem_wireless_model_reference/P044_modem_backend_uart_async_结构体.md#a85e0e51366bbb2e1d7a72e0b9a0650ee)
- [modem_backend_uart_async::common](../modem_wireless_model_reference/P044_modem_backend_uart_async_结构体.md#a8c186bed442db94aa84bf76ad3253fc2)
- [modem_backend_uart_async::receive_bufs](../modem_wireless_model_reference/P044_modem_backend_uart_async_结构体.md#a8e6ff3cae3a79e8b26e67282bb50f5ad)
- [modem_backend_uart_async::receive_rb_lock](../modem_wireless_model_reference/P044_modem_backend_uart_async_结构体.md#ab61b263cdbe9bfb796f3dd6ed69b3dea)
- [modem_backend_uart_async::receive_rb](../modem_wireless_model_reference/P044_modem_backend_uart_async_结构体.md#ac3909d735bfecac46001f1b289e222a2)
- [modem_backend_uart_config::receive_buf_size](../modem_wireless_model_reference/P046_modem_backend_uart_config_结构体.md#a2576f671e21a1fa75163ac63ac5e56a4)
- [modem_backend_uart_config::dtr_gpio](../modem_wireless_model_reference/P046_modem_backend_uart_config_结构体.md#a3dad78dbaddbdc94c57f5381d9a5c68f)
- [modem_backend_uart_config::transmit_buf_size](../modem_wireless_model_reference/P046_modem_backend_uart_config_结构体.md#a48c4a5e9de64bcb435d9b8aea05bfd87)
- [modem_backend_uart_config::uart](../modem_wireless_model_reference/P046_modem_backend_uart_config_结构体.md#a4f8752a33e75164370a8eb81615c2555)
- [modem_backend_uart_config::transmit_buf](../modem_wireless_model_reference/P046_modem_backend_uart_config_结构体.md#a64f82b3b4bf6d1ff6081ac075b67a0b0)
- [modem_backend_uart_config::receive_buf](../modem_wireless_model_reference/P046_modem_backend_uart_config_结构体.md#ad80a5bd5efcf37931503049ac2ba788d)
- [modem_backend_uart_isr::receive_buf_len](../modem_wireless_model_reference/P047_modem_backend_uart_isr_结构体.md#a2c50ecd1dad68ee2aa2ad57b1b746831)
- [modem_backend_uart_isr::transmit_buf_put_limit](../modem_wireless_model_reference/P047_modem_backend_uart_isr_结构体.md#a3b0413caf39e82a52e2bbab6ba42ac3b)
- [modem_backend_uart_isr::transmit_buf_len](../modem_wireless_model_reference/P047_modem_backend_uart_isr_结构体.md#a4d270cc8e2260c349c588109a3c4ddae)
- [modem_backend_uart_isr::transmit_rb](../modem_wireless_model_reference/P047_modem_backend_uart_isr_结构体.md#a69aa3fbffb2bfbd8d5ca16effb8f4f17)
- [modem_backend_uart_isr::receive_rdb_used](../modem_wireless_model_reference/P047_modem_backend_uart_isr_结构体.md#ac7a373618e4dc5dfda02bbc9d09a11a3)
- [modem_backend_uart_isr::receive_rdb](../modem_wireless_model_reference/P047_modem_backend_uart_isr_结构体.md#afacd3e6c890a30188987e6cffae03981)
- [modem_backend_uart::uart](../modem_wireless_model_reference/P043_modem_backend_uart_结构体.md#a26f3331f0ae7d9384f369ae50694090d)
- [modem_backend_uart::receive_ready_work](../modem_wireless_model_reference/P043_modem_backend_uart_结构体.md#a369c5fd2072e42f5eedfe03a5d312ec6)
- [modem_backend_uart::async](../modem_wireless_model_reference/P043_modem_backend_uart_结构体.md#a387327d6378834136fe6a0e80cec7337)
- [modem_backend_uart::isr](../modem_wireless_model_reference/P043_modem_backend_uart_结构体.md#a812165945d6a4aba4fd6bc5ba26b3082)
- [modem_backend_uart::transmit_idle_work](../modem_wireless_model_reference/P043_modem_backend_uart_结构体.md#aafd345ff47cc51a9e1100604a51f6b2d)
- [modem_backend_uart::dtr_gpio](../modem_wireless_model_reference/P043_modem_backend_uart_结构体.md#abdf5e8696db6f2732359000abbd60dca)
- [modem_backend_uart::pipe](../modem_wireless_model_reference/P043_modem_backend_uart_结构体.md#af7e0483a6398b6893ac4693e2bc12f31)

---

[上一章](P115_mman.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P117_mpipe_player.h_源码浏览.md)
