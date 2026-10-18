---
id: learning.zephyr-docs.api-source-reference.page-313
title: hdr_ddr.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/hdr__ddr_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第313章\_hdr\_ddr.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/hdr__ddr_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/hdr__ddr_8h.html)。

## 313.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
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
<a id="foldopen00041"></a>
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
<a id="foldopen00102"></a>
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
<a id="l00130"></a>
<a id="l00131"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__ft8xx__reference__api_html_gacde1ca3945cbe6c828f65051c5c3a615"></a>
<a id="agroup__i3c__hdr__ddr_html_ga11e788383aeb52184fdd6483cf702d40"></a>
<a id="agroup__i3c__hdr__ddr_html_ga9bf00a59c3c08f4bf1ffd5ae32c0fad8"></a>
<a id="agroup__i3c__hdr__ddr_html_gaa752f1095c84ad1b94fb09cc0aeee4fa"></a>
<a id="agroup__i3c__transfer__api_html_ga067c0f1e3c9abb6ef34ce48cb7e45cb8"></a>
<a id="agroup__i3c__transfer__api_html_ga0d4ae269a53af945837d158f638d8b5c"></a>
<a id="agroup__i3c__transfer__api_html_ga6ba89782a8646f96dc1f9fa3b9cd2058"></a>
<a id="agroup__i3c__transfer__api_html_ga72f9fb65d218521ad006febf3dd6851b"></a>
<a id="agroup__i3c__transfer__api_html_gac7386b21323d30148bd9456b9d180d7a"></a>
<a id="agroup__i3c__transfer__api_html_gad827935caf8503aeaedd1aceb53d4e38"></a>
<a id="agroup__i3c__transfer__api_html_gad9ff03f4fdcb117b90c17d667a49c295"></a>
<a id="ai3c_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructi3c__device__desc_html"></a>
<a id="astructi3c__msg_html"></a>
<a id="astructi3c__msg_html_a05113fb61ebbc95ded15fcfe374c0217"></a>
<a id="astructi3c__msg_html_a53f5ef80b2cf467e9ff557be7cc568c9"></a>
<a id="astructi3c__msg_html_aa9d8920782b1a024b70970d60886deff"></a>
<a id="astructi3c__msg_html_acab199ec89bfa84915c66e71c872a40b"></a>
<a id="astructi3c__msg_html_ada6582cdd126f36e64f17f66ae3817f0"></a>

```c
/*
 * Copyright 2024 Meta Platforms
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_I3C_HDR_DDR_H_
#define ZEPHYR_INCLUDE_DRIVERS_I3C_HDR_DDR_H_


#include <errno.h>
#include <stddef.h>
#include <stdint.h>

#include <zephyr/drivers/i3c.h>

#ifdef __cplusplus
extern "C" {
#endif

static inline int i3c_hdr_ddr_write(struct i3c_device_desc *target, uint8_t cmd, uint8_t *buf,
                                    uint32_t num_bytes)
{
        struct i3c_msg msg;

        msg.buf = buf;
        msg.len = num_bytes;
        msg.flags = I3C_MSG_WRITE | I3C_MSG_STOP | I3C_MSG_HDR;
        msg.hdr_mode = I3C_MSG_HDR_DDR;
        msg.hdr_cmd_code = cmd;

        return i3c_transfer(target, &msg, 1);
}

static inline int i3c_hdr_ddr_read(struct i3c_device_desc *target, uint8_t cmd, uint8_t *buf,
                                   uint32_t num_bytes)
{
        struct i3c_msg msg;

        msg.buf = buf;
        msg.len = num_bytes;
        msg.flags = I3C_MSG_READ | I3C_MSG_STOP | I3C_MSG_HDR;
        msg.hdr_mode = I3C_MSG_HDR_DDR;
        msg.hdr_cmd_code = cmd;

        return i3c_transfer(target, &msg, 1);
}

static inline int i3c_hdr_ddr_write_read(struct i3c_device_desc *target, const void *write_buf,
                                         size_t num_write, uint8_t read_cmd, void *read_buf,
                                         size_t num_read, uint8_t write_cmd)
{
        struct i3c_msg msg[2];

        msg[0].buf = (uint8_t *)write_buf;
        msg[0].len = num_write;
        msg[0].flags = I3C_MSG_WRITE | I3C_MSG_HDR;
        msg[0].hdr_mode = I3C_MSG_HDR_DDR;
        msg[0].hdr_cmd_code = write_cmd;

        msg[1].buf = (uint8_t *)read_buf;
        msg[1].len = num_read;
        msg[1].flags = I3C_MSG_RESTART | I3C_MSG_READ | I3C_MSG_HDR | I3C_MSG_STOP;
        msg[1].hdr_mode = I3C_MSG_HDR_DDR;
        msg[1].hdr_cmd_code = read_cmd;

        return i3c_transfer(target, msg, 2);
}

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DRIVERS_I3C_HDR_DDR_H_ */
```

## 313.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2024 Meta Platforms。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 131 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_I3C_HDR_DDR_H_`。

## 313.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/hdr__ddr_8h.html)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/drivers/i3c.h](https://docs.zephyrproject.org/latest/doxygen/html/i3c_8h.html)
- [i3c_hdr_ddr_write](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__hdr__ddr.html#ga9bf00a59c3c08f4bf1ffd5ae32c0fad8)
- [i3c_device_desc](../hardware/P401_I3C设备描述符.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [i3c_msg](../hardware/P395_I3C传输消息.md)
- [buf](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__msg.html#aa9d8920782b1a024b70970d60886deff)
- [len](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__msg.html#ada6582cdd126f36e64f17f66ae3817f0)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__msg.html#a05113fb61ebbc95ded15fcfe374c0217)
- [I3C_MSG_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#ga72f9fb65d218521ad006febf3dd6851b)
- [I3C_MSG_STOP](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#ga0d4ae269a53af945837d158f638d8b5c)
- [I3C_MSG_HDR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#gad827935caf8503aeaedd1aceb53d4e38)
- [hdr_mode](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__msg.html#a53f5ef80b2cf467e9ff557be7cc568c9)
- [I3C_MSG_HDR_DDR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#gac7386b21323d30148bd9456b9d180d7a)
- [hdr_cmd_code](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__msg.html#acab199ec89bfa84915c66e71c872a40b)
- [i3c_transfer](../hardware/P394_I3C传输接口.md#ga067c0f1e3c9abb6ef34ce48cb7e45cb8)
- [i3c_hdr_ddr_read](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__hdr__ddr.html#ga11e788383aeb52184fdd6483cf702d40)
- [I3C_MSG_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#ga6ba89782a8646f96dc1f9fa3b9cd2058)
- [i3c_hdr_ddr_write_read](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__hdr__ddr.html#gaa752f1095c84ad1b94fb09cc0aeee4fa)
- [I3C_MSG_RESTART](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#gad9ff03f4fdcb117b90c17d667a49c295)
- [i3c.h](https://docs.zephyrproject.org/latest/doxygen/html/i3c_8h.html)
- [i3c_msg::flags](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__msg.html#a05113fb61ebbc95ded15fcfe374c0217)
- [i3c_msg::hdr_mode](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__msg.html#a53f5ef80b2cf467e9ff557be7cc568c9)
- [i3c_msg::buf](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__msg.html#aa9d8920782b1a024b70970d60886deff)
- [i3c_msg::hdr_cmd_code](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__msg.html#acab199ec89bfa84915c66e71c872a40b)
- [i3c_msg::len](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__msg.html#ada6582cdd126f36e64f17f66ae3817f0)

---

[上一章](P312_hci_raw.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P314_health_cli.h_源码浏览.md)
