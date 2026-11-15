---
id: learning.zephyr-docs.api-source-reference.page-68
title: blob.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/blob_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第68章\_blob.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/blob_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/blob_8h.html)。

## 68.1\_原始可见代码（Source Code）

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
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="foldopen00035"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="foldopen00047"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="foldopen00063"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00069"></a>
<a id="l00074"></a>
<a id="l00079"></a>
<a id="l00083"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00090"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="foldopen00104"></a>
<a id="l00104"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="l00110"></a>
<a id="l00112"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="foldopen00119"></a>
<a id="l00119"></a>
<a id="l00121"></a>
<a id="l00123"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="foldopen00129"></a>
<a id="l00129"></a>
<a id="l00131"></a>
<a id="l00133"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="foldopen00143"></a>
<a id="l00143"></a>
<a id="l00145"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="foldopen00151"></a>
<a id="l00151"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="agroup__bt__mesh__blob_html_ga2618fb7365f180a73a7eecd11cf2f962"></a>
<a id="agroup__bt__mesh__blob_html_ga26ed2c64bae03758a8a53b28052d0f81"></a>
<a id="agroup__bt__mesh__blob_html_ga4e1ea17e8a8ffd42f62d64286ddc576e"></a>
<a id="agroup__bt__mesh__blob_html_ga7b5e2895a6577103a8a680a94ee7776d"></a>
<a id="agroup__bt__mesh__blob_html_gae0cb28c0e50d02f6e003062457053618"></a>
<a id="agroup__bt__mesh__blob_html_gga2618fb7365f180a73a7eecd11cf2f962a1ff9191c6d593881a4a32826323d9aab"></a>
<a id="agroup__bt__mesh__blob_html_gga2618fb7365f180a73a7eecd11cf2f962ae7ded7a63b8fc889a8063b156337081a"></a>
<a id="agroup__bt__mesh__blob_html_gga26ed2c64bae03758a8a53b28052d0f81a19aebd2c4bfb7295a42577fb118771f1"></a>
<a id="agroup__bt__mesh__blob_html_gga26ed2c64bae03758a8a53b28052d0f81a60d2a7f950f2763ecb38b0cd84ae9600"></a>
<a id="agroup__bt__mesh__blob_html_gga26ed2c64bae03758a8a53b28052d0f81a68f54acdddf2df36f31c8c7c4d7eb9b9"></a>
<a id="agroup__bt__mesh__blob_html_gga26ed2c64bae03758a8a53b28052d0f81a9e9c6d6e450d7bfa1290bad777a740bf"></a>
<a id="agroup__bt__mesh__blob_html_gga26ed2c64bae03758a8a53b28052d0f81ae6824f0459de25d00f8c591d6ad5f4fd"></a>
<a id="agroup__bt__mesh__blob_html_gga26ed2c64bae03758a8a53b28052d0f81af6fa22460b1671383a9c4ae4cf1b6581"></a>
<a id="agroup__bt__mesh__blob_html_gga7b5e2895a6577103a8a680a94ee7776da11bd387885e987335df8ddcdc8f3484f"></a>
<a id="agroup__bt__mesh__blob_html_gga7b5e2895a6577103a8a680a94ee7776da1a01794b9fbef5f89355ac9134073ec1"></a>
<a id="agroup__bt__mesh__blob_html_gga7b5e2895a6577103a8a680a94ee7776da1c37502c32d21c669a7a7da2574b068b"></a>
<a id="agroup__bt__mesh__blob_html_gga7b5e2895a6577103a8a680a94ee7776da2653f1c27fab5b789a3091fad35b161e"></a>
<a id="agroup__bt__mesh__blob_html_gga7b5e2895a6577103a8a680a94ee7776da4044bc0cf8f8085975ad4659ae1b12fa"></a>
<a id="agroup__bt__mesh__blob_html_gga7b5e2895a6577103a8a680a94ee7776da996b6fe3e24a560aac0ea54eb7a3f768"></a>
<a id="agroup__bt__mesh__blob_html_gga7b5e2895a6577103a8a680a94ee7776daa51d478f00ff98870c25edde0a27bdcb"></a>
<a id="agroup__bt__mesh__blob_html_gga7b5e2895a6577103a8a680a94ee7776daac639c3c82cf48a394c13e3b057c9c0d"></a>
<a id="agroup__bt__mesh__blob_html_gga7b5e2895a6577103a8a680a94ee7776dac56e3b5bc5eb558470735014dd438f8a"></a>
<a id="agroup__bt__mesh__blob_html_gga7b5e2895a6577103a8a680a94ee7776daca14a1b6e8ce3fd82198b2cc4948aab0"></a>
<a id="agroup__bt__mesh__blob_html_gga7b5e2895a6577103a8a680a94ee7776dafad7fd6bc121da2ed8e78fcfea22a009"></a>
<a id="agroup__bt__mesh__blob_html_ggae0cb28c0e50d02f6e003062457053618a4f9303c1f20e97987d2932e5d86ffe9b"></a>
<a id="agroup__bt__mesh__blob_html_ggae0cb28c0e50d02f6e003062457053618a7906e4fe51f88a5efcb45ada83b7b089"></a>
<a id="agroup__bt__mesh__blob_html_ggae0cb28c0e50d02f6e003062457053618a98cf4939114c3662fe4f659260d076d6"></a>
<a id="agroup__bt__mesh__blob_html_ggae0cb28c0e50d02f6e003062457053618abc015f3e32c34808b86dd39381b810fd"></a>
<a id="agroup__sys-util_html_gae664e7492e37d324831caf2321ddda37"></a>
<a id="akernel_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html_a98a5cc5f4a350bf5652565021a2f239f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructbt__mesh__blob__block_html"></a>
<a id="astructbt__mesh__blob__block_html_a57f92c3b0ef68128d44a90802788dfa3"></a>
<a id="astructbt__mesh__blob__block_html_a67632460e4a37407074105f8ff3f97fd"></a>
<a id="astructbt__mesh__blob__block_html_a6bd9a432a789edeafc5d425232a32b4e"></a>
<a id="astructbt__mesh__blob__block_html_a7521b8121a2a1f280d14e9e222b7d6cf"></a>
<a id="astructbt__mesh__blob__block_html_ad7527108bd3e41a3965bff0ab3ee82b1"></a>
<a id="astructbt__mesh__blob__chunk_html"></a>
<a id="astructbt__mesh__blob__chunk_html_aabd55d7c8acf726cbc3470af55cb6bc5"></a>
<a id="astructbt__mesh__blob__chunk_html_ad6f5ff266346af1ab0ba29f5339cb83f"></a>
<a id="astructbt__mesh__blob__chunk_html_afd2be87f4cd91f29eb24ebd0dfd9bccb"></a>
<a id="astructbt__mesh__blob__io_html"></a>
<a id="astructbt__mesh__blob__io_html_a330ec5dcc8d18b84e7fdab9ef6d75f49"></a>
<a id="astructbt__mesh__blob__io_html_a4666a3fafde0ee9fdd51d27732bec6bc"></a>
<a id="astructbt__mesh__blob__io_html_a57381249bf63924b2345ece6e12909cb"></a>
<a id="astructbt__mesh__blob__io_html_a900f049b6a778d9e0973ee66b46dc046"></a>
<a id="astructbt__mesh__blob__io_html_aac42902d0bbbef10a5e9cc35e8a3ea64"></a>
<a id="astructbt__mesh__blob__io_html_ae0b27ea814e5c939d708ae20d452ca09"></a>
<a id="astructbt__mesh__blob__xfer_html"></a>
<a id="astructbt__mesh__blob__xfer_html_a2c3d9365b5cb6e569d147acae7a74ed6"></a>
<a id="astructbt__mesh__blob__xfer_html_a646c5c56d5290f6c65e2b9fca89e9835"></a>
<a id="astructbt__mesh__blob__xfer_html_a7a2ca36b08d1d55c2dfbca0120a5274d"></a>
<a id="astructbt__mesh__blob__xfer_html_a9b4f37addd1271e26ab90c6e63608867"></a>
<a id="astructbt__mesh__blob__xfer_html_aa971742f85ccd94bbdef6c61203caeba"></a>

```c
/*
 * Copyright (c) 2020 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_BLUETOOTH_MESH_BLOB_H__
#define ZEPHYR_INCLUDE_BLUETOOTH_MESH_BLOB_H__

#include <sys/types.h>

#include <zephyr/kernel.h>

#ifdef __cplusplus
extern "C" {
#endif


#ifndef CONFIG_BT_MESH_BLOB_CHUNK_COUNT_MAX
#define CONFIG_BT_MESH_BLOB_CHUNK_COUNT_MAX 0
#endif

enum bt_mesh_blob_xfer_mode {
        BT_MESH_BLOB_XFER_MODE_NONE,
        BT_MESH_BLOB_XFER_MODE_PUSH,
        BT_MESH_BLOB_XFER_MODE_PULL,
        BT_MESH_BLOB_XFER_MODE_ALL,
};

enum bt_mesh_blob_xfer_phase {
        BT_MESH_BLOB_XFER_PHASE_INACTIVE,
        BT_MESH_BLOB_XFER_PHASE_WAITING_FOR_START,
        BT_MESH_BLOB_XFER_PHASE_WAITING_FOR_BLOCK,
        BT_MESH_BLOB_XFER_PHASE_WAITING_FOR_CHUNK,
        BT_MESH_BLOB_XFER_PHASE_COMPLETE,
        BT_MESH_BLOB_XFER_PHASE_SUSPENDED,
};

enum bt_mesh_blob_status {
        BT_MESH_BLOB_SUCCESS,
        BT_MESH_BLOB_ERR_INVALID_BLOCK_NUM,
        BT_MESH_BLOB_ERR_INVALID_BLOCK_SIZE,
        BT_MESH_BLOB_ERR_INVALID_CHUNK_SIZE,
        BT_MESH_BLOB_ERR_WRONG_PHASE,
        BT_MESH_BLOB_ERR_INVALID_PARAM,
        BT_MESH_BLOB_ERR_WRONG_BLOB_ID,
        BT_MESH_BLOB_ERR_BLOB_TOO_LARGE,
        BT_MESH_BLOB_ERR_UNSUPPORTED_MODE,
        BT_MESH_BLOB_ERR_INTERNAL,
        BT_MESH_BLOB_ERR_INFO_UNAVAILABLE,
};

struct bt_mesh_blob_block {
        size_t size;
        off_t offset;
        uint16_t number;
        uint16_t chunk_count;
        uint8_t missing[DIV_ROUND_UP(CONFIG_BT_MESH_BLOB_CHUNK_COUNT_MAX,
                                         8)];
};

struct bt_mesh_blob_chunk {
        off_t offset;
        size_t size;
        uint8_t *data;
};

struct bt_mesh_blob_xfer {
        uint64_t id;
        size_t size;
        enum bt_mesh_blob_xfer_mode mode;
        /* Logarithmic representation of the block size. */
        uint8_t block_size_log;
        uint16_t chunk_size;
};

enum bt_mesh_blob_io_mode {
        BT_MESH_BLOB_READ,
        BT_MESH_BLOB_WRITE,
};

struct bt_mesh_blob_io {
        int (*open)(const struct bt_mesh_blob_io *io,
                    const struct bt_mesh_blob_xfer *xfer,
                    enum bt_mesh_blob_io_mode mode);

        void (*close)(const struct bt_mesh_blob_io *io,
                      const struct bt_mesh_blob_xfer *xfer);

        int (*block_start)(const struct bt_mesh_blob_io *io,
                           const struct bt_mesh_blob_xfer *xfer,
                           const struct bt_mesh_blob_block *block);

        void (*block_end)(const struct bt_mesh_blob_io *io,
                          const struct bt_mesh_blob_xfer *xfer,
                          const struct bt_mesh_blob_block *block);

        int (*wr)(const struct bt_mesh_blob_io *io,
                  const struct bt_mesh_blob_xfer *xfer,
                  const struct bt_mesh_blob_block *block,
                  const struct bt_mesh_blob_chunk *chunk);

        int (*rd)(const struct bt_mesh_blob_io *io,
                  const struct bt_mesh_blob_xfer *xfer,
                  const struct bt_mesh_blob_block *block,
                  const struct bt_mesh_blob_chunk *chunk);
};


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_MESH_BLOB_H__ */
```

## 68.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2020 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 136 行

块大小的对数表示（Logarithmic representation of block size）。

### 注释 3：原第 270 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_MESH_BLOB_H__`。

## 68.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/blob_8h.html)
- [sys/types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [bt_mesh_blob_xfer_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gae0cb28c0e50d02f6e003062457053618)
- [BT_MESH_BLOB_XFER_MODE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#ggae0cb28c0e50d02f6e003062457053618a98cf4939114c3662fe4f659260d076d6)
- [BT_MESH_BLOB_XFER_MODE_PUSH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#ggae0cb28c0e50d02f6e003062457053618a4f9303c1f20e97987d2932e5d86ffe9b)
- [BT_MESH_BLOB_XFER_MODE_PULL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#ggae0cb28c0e50d02f6e003062457053618abc015f3e32c34808b86dd39381b810fd)
- [BT_MESH_BLOB_XFER_MODE_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#ggae0cb28c0e50d02f6e003062457053618a7906e4fe51f88a5efcb45ada83b7b089)
- [bt_mesh_blob_xfer_phase](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#ga26ed2c64bae03758a8a53b28052d0f81)
- [BT_MESH_BLOB_XFER_PHASE_INACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga26ed2c64bae03758a8a53b28052d0f81a60d2a7f950f2763ecb38b0cd84ae9600)
- [BT_MESH_BLOB_XFER_PHASE_WAITING_FOR_START](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga26ed2c64bae03758a8a53b28052d0f81a68f54acdddf2df36f31c8c7c4d7eb9b9)
- [BT_MESH_BLOB_XFER_PHASE_WAITING_FOR_BLOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga26ed2c64bae03758a8a53b28052d0f81a19aebd2c4bfb7295a42577fb118771f1)
- [BT_MESH_BLOB_XFER_PHASE_WAITING_FOR_CHUNK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga26ed2c64bae03758a8a53b28052d0f81af6fa22460b1671383a9c4ae4cf1b6581)
- [BT_MESH_BLOB_XFER_PHASE_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga26ed2c64bae03758a8a53b28052d0f81ae6824f0459de25d00f8c591d6ad5f4fd)
- [BT_MESH_BLOB_XFER_PHASE_SUSPENDED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga26ed2c64bae03758a8a53b28052d0f81a9e9c6d6e450d7bfa1290bad777a740bf)
- [bt_mesh_blob_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#ga7b5e2895a6577103a8a680a94ee7776d)
- [BT_MESH_BLOB_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga7b5e2895a6577103a8a680a94ee7776daac639c3c82cf48a394c13e3b057c9c0d)
- [BT_MESH_BLOB_ERR_INVALID_BLOCK_NUM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga7b5e2895a6577103a8a680a94ee7776da2653f1c27fab5b789a3091fad35b161e)
- [BT_MESH_BLOB_ERR_INVALID_BLOCK_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga7b5e2895a6577103a8a680a94ee7776dac56e3b5bc5eb558470735014dd438f8a)
- [BT_MESH_BLOB_ERR_INVALID_CHUNK_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga7b5e2895a6577103a8a680a94ee7776dafad7fd6bc121da2ed8e78fcfea22a009)
- [BT_MESH_BLOB_ERR_WRONG_PHASE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga7b5e2895a6577103a8a680a94ee7776da4044bc0cf8f8085975ad4659ae1b12fa)
- [BT_MESH_BLOB_ERR_INVALID_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga7b5e2895a6577103a8a680a94ee7776daca14a1b6e8ce3fd82198b2cc4948aab0)
- [BT_MESH_BLOB_ERR_WRONG_BLOB_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga7b5e2895a6577103a8a680a94ee7776da1c37502c32d21c669a7a7da2574b068b)
- [BT_MESH_BLOB_ERR_BLOB_TOO_LARGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga7b5e2895a6577103a8a680a94ee7776da11bd387885e987335df8ddcdc8f3484f)
- [BT_MESH_BLOB_ERR_UNSUPPORTED_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga7b5e2895a6577103a8a680a94ee7776da996b6fe3e24a560aac0ea54eb7a3f768)
- [BT_MESH_BLOB_ERR_INTERNAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga7b5e2895a6577103a8a680a94ee7776daa51d478f00ff98870c25edde0a27bdcb)
- [BT_MESH_BLOB_ERR_INFO_UNAVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga7b5e2895a6577103a8a680a94ee7776da1a01794b9fbef5f89355ac9134073ec1)
- [bt_mesh_blob_block](../bluetooth_mesh_model_reference/P001_bt_mesh_blob_block_结构体.md)
- [size](../bluetooth_mesh_model_reference/P001_bt_mesh_blob_block_结构体.md#a67632460e4a37407074105f8ff3f97fd)
- [off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)
- [offset](../bluetooth_mesh_model_reference/P001_bt_mesh_blob_block_结构体.md#a7521b8121a2a1f280d14e9e222b7d6cf)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [number](../bluetooth_mesh_model_reference/P001_bt_mesh_blob_block_结构体.md#a57f92c3b0ef68128d44a90802788dfa3)
- [chunk_count](../bluetooth_mesh_model_reference/P001_bt_mesh_blob_block_结构体.md#a6bd9a432a789edeafc5d425232a32b4e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [missing](../bluetooth_mesh_model_reference/P001_bt_mesh_blob_block_结构体.md#ad7527108bd3e41a3965bff0ab3ee82b1)
- [DIV_ROUND_UP](../util_reference/P001_通用工具公共接口.md#gae664e7492e37d324831caf2321ddda37)
- [CONFIG_BT_MESH_BLOB_CHUNK_COUNT_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#ga4e1ea17e8a8ffd42f62d64286ddc576e)
- [bt_mesh_blob_chunk](../bluetooth_mesh_model_reference/P002_bt_mesh_blob_chunk_结构体.md)
- [offset](../bluetooth_mesh_model_reference/P002_bt_mesh_blob_chunk_结构体.md#aabd55d7c8acf726cbc3470af55cb6bc5)
- [size](../bluetooth_mesh_model_reference/P002_bt_mesh_blob_chunk_结构体.md#afd2be87f4cd91f29eb24ebd0dfd9bccb)
- [data](../bluetooth_mesh_model_reference/P002_bt_mesh_blob_chunk_结构体.md#ad6f5ff266346af1ab0ba29f5339cb83f)
- [bt_mesh_blob_xfer](../bluetooth_mesh_model_reference/P014_bt_mesh_blob_xfer_结构体.md)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [id](../bluetooth_mesh_model_reference/P014_bt_mesh_blob_xfer_结构体.md#a9b4f37addd1271e26ab90c6e63608867)
- [size](../bluetooth_mesh_model_reference/P014_bt_mesh_blob_xfer_结构体.md#a7a2ca36b08d1d55c2dfbca0120a5274d)
- [mode](../bluetooth_mesh_model_reference/P014_bt_mesh_blob_xfer_结构体.md#a2c3d9365b5cb6e569d147acae7a74ed6)
- [block_size_log](../bluetooth_mesh_model_reference/P014_bt_mesh_blob_xfer_结构体.md#aa971742f85ccd94bbdef6c61203caeba)
- [chunk_size](../bluetooth_mesh_model_reference/P014_bt_mesh_blob_xfer_结构体.md#a646c5c56d5290f6c65e2b9fca89e9835)
- [bt_mesh_blob_io_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#ga2618fb7365f180a73a7eecd11cf2f962)
- [BT_MESH_BLOB_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga2618fb7365f180a73a7eecd11cf2f962ae7ded7a63b8fc889a8063b156337081a)
- [BT_MESH_BLOB_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga2618fb7365f180a73a7eecd11cf2f962a1ff9191c6d593881a4a32826323d9aab)
- [bt_mesh_blob_io](../bluetooth_mesh_model_reference/P007_bt_mesh_blob_io_结构体.md)
- [open](../bluetooth_mesh_model_reference/P007_bt_mesh_blob_io_结构体.md#a4666a3fafde0ee9fdd51d27732bec6bc)
- [close](../bluetooth_mesh_model_reference/P007_bt_mesh_blob_io_结构体.md#aac42902d0bbbef10a5e9cc35e8a3ea64)
- [block_start](../bluetooth_mesh_model_reference/P007_bt_mesh_blob_io_结构体.md#a900f049b6a778d9e0973ee66b46dc046)
- [block_end](../bluetooth_mesh_model_reference/P007_bt_mesh_blob_io_结构体.md#a57381249bf63924b2345ece6e12909cb)
- [wr](../bluetooth_mesh_model_reference/P007_bt_mesh_blob_io_结构体.md#ae0b27ea814e5c939d708ae20d452ca09)
- [rd](../bluetooth_mesh_model_reference/P007_bt_mesh_blob_io_结构体.md#a330ec5dcc8d18b84e7fdab9ef6d75f49)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)
- [bt_mesh_blob_block::number](../bluetooth_mesh_model_reference/P001_bt_mesh_blob_block_结构体.md#a57f92c3b0ef68128d44a90802788dfa3)
- [bt_mesh_blob_block::size](../bluetooth_mesh_model_reference/P001_bt_mesh_blob_block_结构体.md#a67632460e4a37407074105f8ff3f97fd)
- [bt_mesh_blob_block::chunk_count](../bluetooth_mesh_model_reference/P001_bt_mesh_blob_block_结构体.md#a6bd9a432a789edeafc5d425232a32b4e)
- [bt_mesh_blob_block::offset](../bluetooth_mesh_model_reference/P001_bt_mesh_blob_block_结构体.md#a7521b8121a2a1f280d14e9e222b7d6cf)
- [bt_mesh_blob_block::missing](../bluetooth_mesh_model_reference/P001_bt_mesh_blob_block_结构体.md#ad7527108bd3e41a3965bff0ab3ee82b1)
- [bt_mesh_blob_chunk::offset](../bluetooth_mesh_model_reference/P002_bt_mesh_blob_chunk_结构体.md#aabd55d7c8acf726cbc3470af55cb6bc5)
- [bt_mesh_blob_chunk::data](../bluetooth_mesh_model_reference/P002_bt_mesh_blob_chunk_结构体.md#ad6f5ff266346af1ab0ba29f5339cb83f)
- [bt_mesh_blob_chunk::size](../bluetooth_mesh_model_reference/P002_bt_mesh_blob_chunk_结构体.md#afd2be87f4cd91f29eb24ebd0dfd9bccb)
- [bt_mesh_blob_io::rd](../bluetooth_mesh_model_reference/P007_bt_mesh_blob_io_结构体.md#a330ec5dcc8d18b84e7fdab9ef6d75f49)
- [bt_mesh_blob_io::open](../bluetooth_mesh_model_reference/P007_bt_mesh_blob_io_结构体.md#a4666a3fafde0ee9fdd51d27732bec6bc)
- [bt_mesh_blob_io::block_end](../bluetooth_mesh_model_reference/P007_bt_mesh_blob_io_结构体.md#a57381249bf63924b2345ece6e12909cb)
- [bt_mesh_blob_io::block_start](../bluetooth_mesh_model_reference/P007_bt_mesh_blob_io_结构体.md#a900f049b6a778d9e0973ee66b46dc046)
- [bt_mesh_blob_io::close](../bluetooth_mesh_model_reference/P007_bt_mesh_blob_io_结构体.md#aac42902d0bbbef10a5e9cc35e8a3ea64)
- [bt_mesh_blob_io::wr](../bluetooth_mesh_model_reference/P007_bt_mesh_blob_io_结构体.md#ae0b27ea814e5c939d708ae20d452ca09)
- [bt_mesh_blob_xfer::mode](../bluetooth_mesh_model_reference/P014_bt_mesh_blob_xfer_结构体.md#a2c3d9365b5cb6e569d147acae7a74ed6)
- [bt_mesh_blob_xfer::chunk_size](../bluetooth_mesh_model_reference/P014_bt_mesh_blob_xfer_结构体.md#a646c5c56d5290f6c65e2b9fca89e9835)
- [bt_mesh_blob_xfer::size](../bluetooth_mesh_model_reference/P014_bt_mesh_blob_xfer_结构体.md#a7a2ca36b08d1d55c2dfbca0120a5274d)
- [bt_mesh_blob_xfer::id](../bluetooth_mesh_model_reference/P014_bt_mesh_blob_xfer_结构体.md#a9b4f37addd1271e26ab90c6e63608867)
- [bt_mesh_blob_xfer::block_size_log](../bluetooth_mesh_model_reference/P014_bt_mesh_blob_xfer_结构体.md#aa971742f85ccd94bbdef6c61203caeba)

---

[上一章](P067_blinfo.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P069_cap.h_源码浏览.md)
