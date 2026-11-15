---
id: learning.zephyr-docs.api-source-reference.page-309
title: hci_lockstep.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/hci__lockstep_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第309章\_hci\_lockstep.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/hci__lockstep_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/hci__lockstep_8h.html)。

## 309.1\_原始可见代码（Source Code）

<a id="l00001"></a>
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
<a id="l00072"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="foldopen00097"></a>
<a id="l00097"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__bt__hci__lockstep_html_ga02ea7a0ad2bbb7d8ee9845122e34f8ab"></a>
<a id="agroup__bt__hci__lockstep_html_ga1d2d42b2db398cf4449b337588897f56"></a>
<a id="agroup__bt__hci__lockstep_html_ga3eeed334ea5d5f212e3b560bd5cd4def"></a>
<a id="agroup__bt__hci__lockstep_html_gaa53d7b9aa5a7d6c5f11ea442c37f75d8"></a>
<a id="agroup__bt__hci__lockstep_html_gacb84fdafc6376483e12a8b7ec391fa7c"></a>
<a id="agroup__ft8xx__reference__api_html_gacde1ca3945cbe6c828f65051c5c3a615"></a>
<a id="ahci__pkt_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="anet__buf_8h_html"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="aposix_2sys_2socket_8h_html_a16485de18b1ec93572e5d74b4a04e42f"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructbt__hci__lockstep_html"></a>
<a id="astructbt__hci__lockstep_html_a6af9d44ebb27dab6971b99c39ba9b747"></a>
<a id="astructdevice_html"></a>
<a id="astructk__sem_html"></a>
<a id="astructk__spinlock_html"></a>
<a id="astructk__timeout__t_html"></a>
<a id="astructnet__buf__simple_html"></a>
<a id="astructnet__buf__simple_html_ae8707c50d70c26b53281b40eb1720cf3"></a>

```c


/*
 * Copyright (c) 2026 Silicon Laboratories Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_BLUETOOTH_HCI_LOCKSTEP_H_
#define ZEPHYR_INCLUDE_DRIVERS_BLUETOOTH_HCI_LOCKSTEP_H_

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

#include <zephyr/bluetooth/hci_pkt.h>
#include <zephyr/device.h>
#include <zephyr/kernel.h>
#include <zephyr/net_buf.h>

#ifdef __cplusplus
extern "C" {
#endif


typedef int (*bt_hci_lockstep_send_t)(const struct device *dev, const uint8_t *pkt, size_t len);

struct bt_hci_lockstep {
        const struct device *dev;
        bt_hci_lockstep_send_t send;
        struct k_sem changed;
        struct k_spinlock lock;
        struct net_buf_simple *rsp;
        uint16_t opcode;
        uint8_t state;
        uint8_t status;

        k_timeout_t timeout;
};

void bt_hci_lockstep_init(struct bt_hci_lockstep *ls, const struct device *dev,
                          bt_hci_lockstep_send_t send);

void bt_hci_lockstep_reset(struct bt_hci_lockstep *ls);

bool bt_hci_lockstep_feed(struct bt_hci_lockstep *ls, const uint8_t *pkt, size_t len);

int bt_hci_lockstep_cmd_send_sync(struct bt_hci_lockstep *ls, uint16_t opcode,
                                  struct net_buf_simple *cmd, struct net_buf_simple *rsp);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_BLUETOOTH_HCI_LOCKSTEP_H_ */
```

## 309.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：© 2026 Silicon Laboratories Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 259 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_BLUETOOTH_HCI_LOCKSTEP_H_`。

## 309.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/hci__lockstep_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/bluetooth/hci_pkt.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__pkt_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [bt_hci_lockstep_send_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__lockstep.html#ga3eeed334ea5d5f212e3b560bd5cd4def)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_hci_lockstep](../bluetooth_hci_model_reference/P326_bt_hci_lockstep_结构体.md)
- [send](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html#a16485de18b1ec93572e5d74b4a04e42f)
- [k_sem](../synchronization_reference/P009_内核信号量结构.md)
- [k_spinlock](../kernel/P066_自旋锁结构参考.md)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [timeout](../bluetooth_hci_model_reference/P326_bt_hci_lockstep_结构体.md#a6af9d44ebb27dab6971b99c39ba9b747)
- [bt_hci_lockstep_init](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__lockstep.html#ga02ea7a0ad2bbb7d8ee9845122e34f8ab)
- [bt_hci_lockstep_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__lockstep.html#ga1d2d42b2db398cf4449b337588897f56)
- [bt_hci_lockstep_feed](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__lockstep.html#gacb84fdafc6376483e12a8b7ec391fa7c)
- [len](../network_core_model_reference/P048_net_buf_simple_结构体.md#ae8707c50d70c26b53281b40eb1720cf3)
- [bt_hci_lockstep_cmd_send_sync](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__lockstep.html#gaa53d7b9aa5a7d6c5f11ea442c37f75d8)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [hci_pkt.h](https://docs.zephyrproject.org/latest/doxygen/html/hci__pkt_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [bt_hci_lockstep::timeout](../bluetooth_hci_model_reference/P326_bt_hci_lockstep_结构体.md#a6af9d44ebb27dab6971b99c39ba9b747)
- [net_buf_simple::len](../network_core_model_reference/P048_net_buf_simple_结构体.md#ae8707c50d70c26b53281b40eb1720cf3)

---

[上一章](P308_hci_driver_bluenrg.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P310_hci_nxp_setup.h_源码浏览.md)
