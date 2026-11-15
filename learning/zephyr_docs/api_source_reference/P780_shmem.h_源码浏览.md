---
id: learning.zephyr-docs.api-source-reference.page-780
title: shmem.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/shmem_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第780章\_shmem.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/shmem_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/shmem_8h.html)。

## 780.1\_原始可见代码（Source Code）

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
<a id="l00026"></a>
<a id="l00028"></a>
<a id="l00033"></a>
<a id="l00038"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="aarch_2cpu_8h_html"></a>
<a id="adevice_8h_html"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__scmi__shmem_html_ga32f0c9fdfca8450b5ab2dc33ce64896c"></a>
<a id="agroup__scmi__shmem_html_ga5e1978cff70bd92d233fdacf7ae0de48"></a>
<a id="agroup__scmi__shmem_html_ga6e2330af169f33b768dcacf5e2dba5a2"></a>
<a id="agroup__scmi__shmem_html_gaa61c9eea220cc353b97c316bc94e0072"></a>
<a id="agroup__scmi__shmem_html_gaab6dca2dc06cb108f40e358479b19426"></a>
<a id="agroup__scmi__shmem_html_gabb1c2c847a723adc45e936e1c771af0d"></a>
<a id="agroup__scmi__shmem_html_gaf0f9657082d02048c2d5df7c14833228"></a>
<a id="agroup__scmi__shmem_html_gaf36f95840d1a62582edcf53e0482aeb5"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructdevice_html"></a>
<a id="astructscmi__message_html"></a>
<a id="astructscmi__message_html_a4b329136651a527d51310af82dc24795"></a>

```c
/*
 * Copyright 2024,2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_FIRMWARE_SCMI_SHMEM_H_
#define ZEPHYR_INCLUDE_DRIVERS_FIRMWARE_SCMI_SHMEM_H_

#include <zephyr/device.h>
#include <zephyr/arch/cpu.h>
#include <errno.h>



#define SCMI_SHMEM_CHAN_STATUS_BUSY_BIT BIT(0)

#define SCMI_SHMEM_CHAN_FLAG_IRQ_BIT BIT(0)

struct scmi_shmem_layout {
        volatile uint32_t res0;
        volatile uint32_t chan_status;
        volatile uint32_t res1[2];
        volatile uint32_t chan_flags;
        volatile uint32_t len;
        volatile uint32_t msg_hdr;
};


struct scmi_message;

int scmi_shmem_write_message(const struct device *shmem,
                             struct scmi_message *msg,
                             bool use_polling);

int scmi_shmem_read_hdr(const struct device *shmem, uint32_t *hdr);

int scmi_shmem_read_message(const struct device *shmem,
                            struct scmi_message *msg);

void scmi_shmem_update_flags(const struct device *shmem,
                             uint32_t mask, uint32_t val);

uint32_t scmi_shmem_channel_status(const struct device *shmem);

int scmi_shmem_vendor_write_message(struct scmi_shmem_layout *layout);

int scmi_shmem_vendor_read_message(const struct scmi_shmem_layout *layout);

void scmi_shmem_mark_channel_free(const struct device *dev);


#endif /* ZEPHYR_INCLUDE_DRIVERS_FIRMWARE_SCMI_SHMEM_H_ */
```

## 780.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2024,2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 154 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_FIRMWARE_SCMI_SHMEM_H_`。

## 780.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/shmem_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/arch/cpu.h](https://docs.zephyrproject.org/latest/doxygen/html/arch_2cpu_8h.html)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [scmi_message](../platform_security_model_reference/P037_scmi_message_结构体.md)
- [scmi_shmem_write_message](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__shmem.html#gaf36f95840d1a62582edcf53e0482aeb5)
- [device](../device_reference/P002_设备对象结构.md)
- [scmi_shmem_read_hdr](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__shmem.html#ga6e2330af169f33b768dcacf5e2dba5a2)
- [hdr](../platform_security_model_reference/P037_scmi_message_结构体.md#a4b329136651a527d51310af82dc24795)
- [scmi_shmem_read_message](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__shmem.html#gaf0f9657082d02048c2d5df7c14833228)
- [scmi_shmem_update_flags](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__shmem.html#gaa61c9eea220cc353b97c316bc94e0072)
- [scmi_shmem_channel_status](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__shmem.html#ga32f0c9fdfca8450b5ab2dc33ce64896c)
- [scmi_shmem_vendor_write_message](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__shmem.html#gaab6dca2dc06cb108f40e358479b19426)
- [scmi_shmem_vendor_read_message](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__shmem.html#ga5e1978cff70bd92d233fdacf7ae0de48)
- [scmi_shmem_mark_channel_free](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__shmem.html#gabb1c2c847a723adc45e936e1c771af0d)
- [cpu.h](https://docs.zephyrproject.org/latest/doxygen/html/arch_2cpu_8h.html)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [scmi_message::hdr](../platform_security_model_reference/P037_scmi_message_结构体.md#a4b329136651a527d51310af82dc24795)

---

[上一章](P779_sgp40.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P781_sht4x.h_源码浏览.md)
