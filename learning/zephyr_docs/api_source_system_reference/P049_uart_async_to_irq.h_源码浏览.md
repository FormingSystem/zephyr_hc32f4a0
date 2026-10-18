---
id: learning.zephyr-docs.api-source-system-reference.page-49
title: uart_async_to_irq.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/uart__async__to__irq_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第49章\_uart\_async\_to\_irq.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/uart__async__to__irq_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../hardware/P360_UART异步转中断接口.md)。

## 49.1\_原始可见代码（Source Code）

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
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00032"></a>
<a id="l00033"></a>
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
<a id="l00054"></a>
<a id="l00055"></a>
<a id="foldopen00061"></a>
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
<a id="l00143"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
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
<a id="l00183"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00195"></a>
<a id="l00197"></a>
<a id="l00198"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00204"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="adrivers_2uart_8h_html"></a>
<a id="agroup__atomic__apis_html_ga124f07c3a788e53c3a40e4e1c06d8af8"></a>
<a id="agroup__log__api_html_ga224e4a75dca6d1b363ef49e96730dcfd"></a>
<a id="agroup__uart__async_html_ga00b7c98a4da3ea3675d0a40c5dacb136"></a>
<a id="agroup__uart__interrupt_html_gad7a26b1a1d6212d7d39c05c8ad4ec926"></a>
<a id="alog_8h_html"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="aspinlock_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructdevice_html"></a>
<a id="astructuart__async__rx__config_html"></a>
<a id="asys_2util_8h_html"></a>
<a id="auart__async__rx_8h_html"></a>
<a id="auart__async__to__irq_8h_html_a42a81b74f16109ad516628f99bc44503"></a>
<a id="auart__async__to__irq_8h_html_a4638b8d0a01c9cd388e5d0dafc9b4d8c"></a>
<a id="auart__async__to__irq_8h_html_a6f9f2a997d3c8b76d3615f1de85b8a92"></a>
<a id="auart__async__to__irq_8h_html_a954f64af4a7fc5b752c21057c87741cf"></a>
<a id="auart__async__to__irq_8h_html_aae442237aa3432348c256807df3ffa1c"></a>

```c
/*
 * Copyright (c) 2023 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_DRIVERS_SERIAL_UART_ASYNC_TO_IRQ_H_
#define ZEPHYR_DRIVERS_SERIAL_UART_ASYNC_TO_IRQ_H_

#include <zephyr/drivers/uart.h>
#include <zephyr/logging/log.h>
#include <zephyr/spinlock.h>
#include <zephyr/sys/util.h>
#include <zephyr/drivers/serial/uart_async_rx.h>


#ifdef __cplusplus
extern "C" {
#endif

/* Forward declarations. */

struct uart_async_to_irq_data;

struct uart_async_to_irq_config;

/* @brief Function that triggers trampoline to the interrupt context.
 *
 * This context is used to call user UART interrupt handler. It is to used to
 * fulfill the requirement that UART interrupt driven API shall be called from
 * the UART interrupt. Trampoline context shall have the same priority as UART.
 *
 * One option may be to use k_timer configured to expire immediately.
 */
typedef void (*uart_async_to_irq_trampoline)(const struct device *dev);

void uart_async_to_irq_trampoline_cb(const struct device *dev);

#define UART_ASYNC_TO_IRQ_API_INIT()                            \
        .fifo_fill        = z_uart_async_to_irq_fifo_fill,      \
        .fifo_read        = z_uart_async_to_irq_fifo_read,      \
        .irq_tx_enable    = z_uart_async_to_irq_irq_tx_enable,  \
        .irq_tx_disable   = z_uart_async_to_irq_irq_tx_disable, \
        .irq_tx_ready     = z_uart_async_to_irq_irq_tx_ready,   \
        .irq_rx_enable    = z_uart_async_to_irq_irq_rx_enable,  \
        .irq_rx_disable   = z_uart_async_to_irq_irq_rx_disable, \
        .irq_tx_complete  = z_uart_async_to_irq_irq_tx_complete,\
        .irq_rx_ready     = z_uart_async_to_irq_irq_rx_ready,   \
        .irq_err_enable   = z_uart_async_to_irq_irq_err_enable, \
        .irq_err_disable  = z_uart_async_to_irq_irq_err_disable,\
        .irq_is_pending   = z_uart_async_to_irq_irq_is_pending, \
        .irq_update       = NULL,                               \
        .irq_callback_set = z_uart_async_to_irq_irq_callback_set

#define UART_ASYNC_TO_IRQ_API_CONFIG_INITIALIZER(_api, _trampoline, _baudrate, _tx_buf,         \
                                                 _tx_len, _rx_buf, _rx_len, _rx_cnt, _log)      \
        {                                                                                       \
                .tx_buf = _tx_buf,                                                              \
                .tx_len = _tx_len,                                                              \
                .async_rx = {                                                                   \
                        .buffer = _rx_buf,                                                      \
                        .length = _rx_len,                                                      \
                        .buf_cnt = _rx_cnt                                                      \
                },                                                                              \
                .api = _api,                                                                    \
                .trampoline = _trampoline,                                                      \
                .baudrate = _baudrate,                                                          \
                LOG_OBJECT_PTR_INIT(log,                                                        \
                                COND_CODE_1(IS_EMPTY(_log),                                     \
                                            (LOG_OBJECT_PTR(UART_ASYNC_TO_IRQ_LOG_NAME)),       \
                                            (_log)                                              \
                                           )                                                    \
                                   )                                                            \
        }

int uart_async_to_irq_init(const struct device *dev);

/* @brief Enable RX for interrupt driven API.
 *
 * @param dev UART device. Device must support asynchronous API.
 *
 * @retval 0 on successful operation.
 * @retval -EINVAL if adaption layer has wrong configuration.
 * @retval negative value Error reported by the UART API.
 */
int uart_async_to_irq_rx_enable(const struct device *dev);

/* @brief Disable RX for interrupt driven API.
 *
 * @param dev UART device. Device must support asynchronous API.
 *
 * @retval 0 on successful operation.
 * @retval -EINVAL if adaption layer has wrong configuration.
 * @retval negative value Error reported by the UART API.
 */
int uart_async_to_irq_rx_disable(const struct device *dev);

/* Starting from here API is internal only. */

struct uart_async_to_irq_config {
        uint8_t *tx_buf;

        size_t tx_len;

        struct uart_async_rx_config async_rx;

        const struct uart_async_to_irq_async_api *api;

        uart_async_to_irq_trampoline trampoline;

        uint32_t baudrate;

        LOG_INSTANCE_PTR_DECLARE(log);
};

struct uart_async_to_irq_async_api {
        int (*callback_set)(const struct device *dev,
                            uart_callback_t callback,
                            void *user_data);

        int (*tx)(const struct device *dev, const uint8_t *buf, size_t len,
                  int32_t timeout);
        int (*tx_abort)(const struct device *dev);

        int (*rx_enable)(const struct device *dev, uint8_t *buf, size_t len,
                         int32_t timeout);
        int (*rx_buf_rsp)(const struct device *dev, uint8_t *buf, size_t len);
        int (*rx_disable)(const struct device *dev);
};

struct uart_async_to_irq_rx_data {
        struct uart_async_rx async_rx;

        struct k_sem sem;

        atomic_t pending_buf_req;
};

struct uart_async_to_irq_tx_data {
        uint8_t *buf;

        size_t len;
};

struct uart_async_to_irq_data {
        uart_irq_callback_user_data_t callback;

        void *user_data;

        atomic_t irq_req;

        struct uart_async_to_irq_rx_data rx;

        struct uart_async_to_irq_tx_data tx;

        struct k_spinlock lock;

        atomic_t flags;
};

int z_uart_async_to_irq_fifo_fill(const struct device *dev,
                                  const uint8_t *buf,
                                  int len);

int z_uart_async_to_irq_fifo_read(const struct device *dev,
                                  uint8_t *buf,
                                  const int len);

void z_uart_async_to_irq_irq_tx_enable(const struct device *dev);

void z_uart_async_to_irq_irq_tx_disable(const struct device *dev);

int z_uart_async_to_irq_irq_tx_ready(const struct device *dev);

void z_uart_async_to_irq_irq_rx_enable(const struct device *dev);

void z_uart_async_to_irq_irq_rx_disable(const struct device *dev);

int z_uart_async_to_irq_irq_tx_complete(const struct device *dev);

int z_uart_async_to_irq_irq_rx_ready(const struct device *dev);

void z_uart_async_to_irq_irq_err_enable(const struct device *dev);

void z_uart_async_to_irq_irq_err_disable(const struct device *dev);

int z_uart_async_to_irq_irq_is_pending(const struct device *dev);

void z_uart_async_to_irq_irq_callback_set(const struct device *dev,
                         uart_irq_callback_user_data_t cb,
                         void *user_data);


#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_DRIVERS_SERIAL_UART_ASYNC_TO_IRQ_H_ */
```

## 49.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 26 行

前向声明（Forward Declarations）。

### 注释 3：原第 40 行

触发跳板（Trampoline）进入中断上下文（Interrupt Context）的函数。

该上下文用于调用用户 UART 中断处理器（Interrupt Handler），以满足 UART 中断驱动 API（Interrupt-Driven API）必须从 UART 中断中调用的要求。跳板上下文的优先级（Priority）必须与 UART 相同。

一种实现方式是使用配置为立即到期（Expire Immediately）的 `k_timer`。

### 注释 4：原第 118 行

为中断驱动 API（Interrupt-Driven API）启用接收（RX）。

参数（`@param`）`dev`：UART 设备，必须支持异步 API（Asynchronous API）。

- 返回值（`@retval`）0：操作成功。
- `-EINVAL`：适配层（Adaptation Layer）配置错误。
- 其他负值：UART API 报告的错误。

### 注释 5：原第 128 行

为中断驱动 API（Interrupt-Driven API）禁用接收（RX）。

参数（`@param`）`dev`：UART 设备，必须支持异步 API（Asynchronous API）。

- 返回值（`@retval`）0：操作成功。
- `-EINVAL`：适配层（Adaptation Layer）配置错误。
- 其他负值：UART API 报告的错误。

### 注释 6：原第 138 行

从这里开始，API 仅供内部使用（Internal Only）。

### 注释 7：原第 280 行

头文件保护宏（Header guard）标记：`ZEPHYR_DRIVERS_SERIAL_UART_ASYNC_TO_IRQ_H_`。

## 49.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../hardware/P360_UART异步转中断接口.md)
- [zephyr/drivers/uart.h](../uart_driver_reference/P001_UART驱动头文件参考.md)
- [zephyr/logging/log.h](../log_core_reference/P003_日志公共头文件参考.md)
- [zephyr/spinlock.h](../kernel/P067_自旋锁头文件参考.md)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [zephyr/drivers/serial/uart_async_rx.h](../hardware/P344_UART异步接收辅助接口.md)
- [uart_async_to_irq_trampoline](https://docs.zephyrproject.org/latest/doxygen/html/uart__async__to__irq_8h.html#a6f9f2a997d3c8b76d3615f1de85b8a92)
- [device](../device_reference/P002_设备对象结构.md)
- [uart_async_to_irq_trampoline_cb](https://docs.zephyrproject.org/latest/doxygen/html/uart__async__to__irq_8h.html#a954f64af4a7fc5b752c21057c87741cf)
- [uart_async_to_irq_init](https://docs.zephyrproject.org/latest/doxygen/html/uart__async__to__irq_8h.html#aae442237aa3432348c256807df3ffa1c)
- [uart_async_to_irq_rx_enable](https://docs.zephyrproject.org/latest/doxygen/html/uart__async__to__irq_8h.html#a42a81b74f16109ad516628f99bc44503)
- [uart_async_to_irq_rx_disable](https://docs.zephyrproject.org/latest/doxygen/html/uart__async__to__irq_8h.html#a4638b8d0a01c9cd388e5d0dafc9b4d8c)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uart_async_rx_config](../hardware/P347_UART异步接收配置结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [LOG_INSTANCE_PTR_DECLARE](../log_core_reference/P002_日志公共接口.md#ga224e4a75dca6d1b363ef49e96730dcfd)
- [uart_callback_t](../hardware/P334_UART异步接口.md#ga00b7c98a4da3ea3675d0a40c5dacb136)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [uart_irq_callback_user_data_t](../hardware/P333_UART中断驱动接口.md#gad7a26b1a1d6212d7d39c05c8ad4ec926)
- [flags](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [uart.h](../uart_driver_reference/P001_UART驱动头文件参考.md)
- [log.h](../log_core_reference/P003_日志公共头文件参考.md)
- [spinlock.h](../kernel/P067_自旋锁头文件参考.md)
- [util.h](../util_reference/P002_通用工具头文件参考.md)
- [uart_async_rx.h](../hardware/P344_UART异步接收辅助接口.md)

---

[上一章](P048_tsl2540.h_源码浏览.md) · [返回大纲](大纲.md)
