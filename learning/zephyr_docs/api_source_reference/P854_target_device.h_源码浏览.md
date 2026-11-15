---
id: learning.zephyr-docs.api-source-reference.page-854
title: target_device.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/target__device_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第854章\_target\_device.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/target__device_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/target__device_8h.html)。

## 854.1\_原始可见代码（Source Code）

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
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="foldopen00036"></a>
<a id="l00036"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="foldopen00101"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="foldopen00106"></a>
<a id="l00106"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00279"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="foldopen00293"></a>
<a id="l00293"></a>
<a id="l00298"></a>
<a id="l00303"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="l00307"></a>
<a id="foldopen00320"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="l00327"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="foldopen00356"></a>
<a id="l00356"></a>
<a id="l00357"></a>
<a id="l00358"></a>
<a id="l00359"></a>
<a id="l00360"></a>
<a id="l00361"></a>
<a id="l00362"></a>
<a id="l00363"></a>
<a id="l00364"></a>
<a id="l00365"></a>
<a id="l00366"></a>
<a id="l00367"></a>
<a id="foldopen00390"></a>
<a id="l00390"></a>
<a id="l00391"></a>
<a id="l00392"></a>
<a id="l00393"></a>
<a id="l00394"></a>
<a id="l00395"></a>
<a id="l00396"></a>
<a id="l00397"></a>
<a id="l00398"></a>
<a id="l00399"></a>
<a id="l00400"></a>
<a id="l00401"></a>
<a id="foldopen00418"></a>
<a id="l00418"></a>
<a id="l00419"></a>
<a id="l00420"></a>
<a id="l00421"></a>
<a id="l00422"></a>
<a id="l00423"></a>
<a id="l00424"></a>
<a id="l00425"></a>
<a id="l00426"></a>
<a id="l00427"></a>
<a id="l00428"></a>
<a id="l00429"></a>
<a id="l00430"></a>
<a id="l00431"></a>
<a id="l00432"></a>
<a id="l00433"></a>
<a id="l00437"></a>
<a id="l00438"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__i3c__target__device__backend_html_ga5b45ad9e1388ac39093cd5374a9f5c4c"></a>
<a id="agroup__i3c__target__device__backend_html_gae6b75cf65f1715ff36bc0aa1a0908b07"></a>
<a id="agroup__i3c__target__device_html_ga09be7f73861bede0071fd8ade344d092"></a>
<a id="agroup__i3c__target__device_html_ga3dc0e6451fb13fa063c5ec3e18fe22e4"></a>
<a id="agroup__i3c__target__device_html_gaf13d2b84a91e17d5ec49a41e9c553d42"></a>
<a id="agroup__i3c__target__device_html_gafb5ebdfd5536ee265a3719beb8ae81dc"></a>
<a id="agroup__system__errno_html_ga43785b9969e0bd1af532dbde06c5540b"></a>
<a id="aposix_2sys_2socket_8h_html_a66e3de379c18201b21c889035ec54864"></a>
<a id="aslist_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructi3c__config__target_html"></a>
<a id="astructi3c__config__target_html_a1d0b97d6428e471bcf9b6945da947b36"></a>
<a id="astructi3c__config__target_html_a25b0837f2363f880936391d9baed1d1e"></a>
<a id="astructi3c__config__target_html_a2ad289658811d142ba9091574acf485b"></a>
<a id="astructi3c__config__target_html_a4339c8dd33b17ce8363bf28177411830"></a>
<a id="astructi3c__config__target_html_a62e1b1a3dff6cc570ecccdfcfc6b196d"></a>
<a id="astructi3c__config__target_html_a78a74f81e632a428db59803b55239419"></a>
<a id="astructi3c__config__target_html_aac5e8a92468df108ce964bb6a9a7ae9c"></a>
<a id="astructi3c__config__target_html_ab5345d23ba2afffbf48010e7edff3c26"></a>
<a id="astructi3c__config__target_html_aca4dc4aa873ca447d06e573d485ab854"></a>
<a id="astructi3c__config__target_html_afaa68c94b35f512a597b35752db8d66e"></a>
<a id="astructi3c__target__callbacks_html"></a>
<a id="astructi3c__target__callbacks_html_a15a1bacdd10c0d6803fbd24f1a1a3323"></a>
<a id="astructi3c__target__callbacks_html_a1e92d1a9bd94b0ef3930bc692764721f"></a>
<a id="astructi3c__target__callbacks_html_a7288f143d19ad306616e25e68ffedc03"></a>
<a id="astructi3c__target__callbacks_html_a9b7ae83ecc4671ea509b4b6f9d01f614"></a>
<a id="astructi3c__target__callbacks_html_abaf52fa6a2189b9e03728a4ae38e66e8"></a>
<a id="astructi3c__target__callbacks_html_ac72e0bab1eeff6995983f90f6d934749"></a>
<a id="astructi3c__target__callbacks_html_ad9e51587a8f86f08d065071d28241ee2"></a>
<a id="astructi3c__target__callbacks_html_ae53661cfa98a3b58a9702fef28234c30"></a>
<a id="astructi3c__target__config_html"></a>
<a id="astructi3c__target__config_html_a43ed9a3679d54f7bb91dade34a5897b6"></a>
<a id="astructi3c__target__driver__api_html"></a>
<a id="astructi3c__target__driver__api_html_a1d1d0426a197b77a5ddc74ffb670b43c"></a>
<a id="astructi3c__target__driver__api_html_ac933f20f1f8affd685f5958c681648c2"></a>

```c
/*
 * Copyright 2022 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_I3C_TARGET_DEVICE_H_
#define ZEPHYR_INCLUDE_DRIVERS_I3C_TARGET_DEVICE_H_


#include <errno.h>
#include <stddef.h>
#include <stdint.h>

#include <zephyr/device.h>
#include <zephyr/sys/slist.h>

#ifdef __cplusplus
extern "C" {
#endif

struct i3c_driver_api;

struct i3c_config_target {
        bool enabled;

        uint8_t dynamic_addr;

        uint8_t static_addr;

        uint64_t pid;

        bool pid_random;

        uint8_t bcr;

        uint8_t dcr;

        uint16_t max_read_len;

        uint16_t max_write_len;

        uint8_t supported_hdr;
};

struct i3c_target_config {
        const struct i3c_target_callbacks *callbacks;
};

struct i3c_target_callbacks {
        int (*write_requested_cb)(struct i3c_target_config *config);

        int (*write_received_cb)(struct i3c_target_config *config,
                                 uint8_t val);

        int (*read_requested_cb)(struct i3c_target_config *config,
                                 uint8_t *val);

        int (*read_processed_cb)(struct i3c_target_config *config,
                                 uint8_t *val);

#if defined(CONFIG_I3C_TARGET_BUFFER_MODE) || defined(__DOXYGEN__)
        void (*buf_write_received_cb)(struct i3c_target_config *config, uint8_t *ptr, uint32_t len);

        int (*buf_read_requested_cb)(struct i3c_target_config *config, uint8_t **ptr, uint32_t *len,
                                     uint8_t *hdr_mode);
#endif /* CONFIG_I3C_TARGET_BUFFER_MODE */

        int (*stop_cb)(struct i3c_target_config *config);

        int (*controller_handoff_cb)(struct i3c_target_config *config);
};


typedef int (*i3c_target_api_driver_register_t)(const struct device *dev);

typedef int (*i3c_target_api_driver_unregister_t)(const struct device *dev);

__subsystem struct i3c_target_driver_api {
        i3c_target_api_driver_register_t driver_register;
        i3c_target_api_driver_unregister_t driver_unregister;
};


static inline int i3c_target_controller_handoff(const struct device *dev,
                                      bool accept)
{
        const struct i3c_driver_api *api = DEVICE_API_GET(i3c, dev);

        if (api->target_controller_handoff == NULL) {
                return -ENOSYS;
        }

        return api->target_controller_handoff(dev, accept);
}

static inline int i3c_target_tx_write(const struct device *dev,
                                      uint8_t *buf, uint16_t len, uint8_t hdr_mode)
{
        const struct i3c_driver_api *api = DEVICE_API_GET(i3c, dev);

        if (api->target_tx_write == NULL) {
                return -ENOSYS;
        }

        return api->target_tx_write(dev, buf, len, hdr_mode);
}

static inline int i3c_target_register(const struct device *dev,
                                      struct i3c_target_config *cfg)
{
        const struct i3c_driver_api *api = DEVICE_API_GET(i3c, dev);

        if (api->target_register == NULL) {
                return -ENOSYS;
        }

        return api->target_register(dev, cfg);
}

static inline int i3c_target_unregister(const struct device *dev,
                                        struct i3c_target_config *cfg)
{
        const struct i3c_driver_api *api = DEVICE_API_GET(i3c, dev);

        if (api->target_unregister == NULL) {
                return -ENOSYS;
        }

        return api->target_unregister(dev, cfg);
}

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DRIVERS_I3C_TARGET_DEVICE_H_ */
```

## 854.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2022 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 239 行

条件编译配置（Configuration）标记：`CONFIG_I3C_TARGET_BUFFER_MODE`。

### 注释 3：原第 438 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_I3C_TARGET_DEVICE_H_`。

## 854.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/target__device_8h.html)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/sys/slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [i3c_config_target](../hardware/P392_I3C目标硬件配置.md)
- [enabled](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__config__target.html#a25b0837f2363f880936391d9baed1d1e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [dynamic_addr](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__config__target.html#aac5e8a92468df108ce964bb6a9a7ae9c)
- [static_addr](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__config__target.html#ab5345d23ba2afffbf48010e7edff3c26)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [pid](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__config__target.html#a62e1b1a3dff6cc570ecccdfcfc6b196d)
- [pid_random](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__config__target.html#a2ad289658811d142ba9091574acf485b)
- [bcr](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__config__target.html#a1d0b97d6428e471bcf9b6945da947b36)
- [dcr](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__config__target.html#afaa68c94b35f512a597b35752db8d66e)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [max_read_len](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__config__target.html#a4339c8dd33b17ce8363bf28177411830)
- [max_write_len](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__config__target.html#aca4dc4aa873ca447d06e573d485ab854)
- [supported_hdr](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__config__target.html#a78a74f81e632a428db59803b55239419)
- [i3c_target_config](../hardware/P388_I3C目标设备配置.md)
- [i3c_target_callbacks](../hardware/P389_I3C目标设备回调表.md)
- [callbacks](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__target__config.html#a43ed9a3679d54f7bb91dade34a5897b6)
- [write_requested_cb](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__target__callbacks.html#ad9e51587a8f86f08d065071d28241ee2)
- [write_received_cb](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__target__callbacks.html#a7288f143d19ad306616e25e68ffedc03)
- [read_requested_cb](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__target__callbacks.html#ac72e0bab1eeff6995983f90f6d934749)
- [read_processed_cb](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__target__callbacks.html#ae53661cfa98a3b58a9702fef28234c30)
- [buf_write_received_cb](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__target__callbacks.html#abaf52fa6a2189b9e03728a4ae38e66e8)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [buf_read_requested_cb](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__target__callbacks.html#a9b7ae83ecc4671ea509b4b6f9d01f614)
- [stop_cb](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__target__callbacks.html#a15a1bacdd10c0d6803fbd24f1a1a3323)
- [controller_handoff_cb](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__target__callbacks.html#a1e92d1a9bd94b0ef3930bc692764721f)
- [i3c_target_api_driver_register_t](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__target__device__backend.html#gae6b75cf65f1715ff36bc0aa1a0908b07)
- [device](../device_reference/P002_设备对象结构.md)
- [i3c_target_api_driver_unregister_t](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__target__device__backend.html#ga5b45ad9e1388ac39093cd5374a9f5c4c)
- [i3c_target_driver_api](../hardware/P390_I3C目标设备驱动函数表.md)
- [driver_register](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__target__driver__api.html#a1d1d0426a197b77a5ddc74ffb670b43c)
- [driver_unregister](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__target__driver__api.html#ac933f20f1f8affd685f5958c681648c2)
- [i3c_target_controller_handoff](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__target__device.html#ga09be7f73861bede0071fd8ade344d092)
- [accept](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html#a66e3de379c18201b21c889035ec54864)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [ENOSYS](../error_reference/P003_系统错误号公共接口.md#ga43785b9969e0bd1af532dbde06c5540b)
- [i3c_target_tx_write](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__target__device.html#gafb5ebdfd5536ee265a3719beb8ae81dc)
- [i3c_target_register](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__target__device.html#gaf13d2b84a91e17d5ec49a41e9c553d42)
- [i3c_target_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__target__device.html#ga3dc0e6451fb13fa063c5ec3e18fe22e4)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [i3c_config_target::bcr](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__config__target.html#a1d0b97d6428e471bcf9b6945da947b36)
- [i3c_config_target::enabled](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__config__target.html#a25b0837f2363f880936391d9baed1d1e)
- [i3c_config_target::pid_random](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__config__target.html#a2ad289658811d142ba9091574acf485b)
- [i3c_config_target::max_read_len](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__config__target.html#a4339c8dd33b17ce8363bf28177411830)
- [i3c_config_target::pid](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__config__target.html#a62e1b1a3dff6cc570ecccdfcfc6b196d)
- [i3c_config_target::supported_hdr](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__config__target.html#a78a74f81e632a428db59803b55239419)
- [i3c_config_target::dynamic_addr](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__config__target.html#aac5e8a92468df108ce964bb6a9a7ae9c)
- [i3c_config_target::static_addr](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__config__target.html#ab5345d23ba2afffbf48010e7edff3c26)
- [i3c_config_target::max_write_len](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__config__target.html#aca4dc4aa873ca447d06e573d485ab854)
- [i3c_config_target::dcr](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__config__target.html#afaa68c94b35f512a597b35752db8d66e)
- [i3c_target_callbacks::stop_cb](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__target__callbacks.html#a15a1bacdd10c0d6803fbd24f1a1a3323)
- [i3c_target_callbacks::controller_handoff_cb](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__target__callbacks.html#a1e92d1a9bd94b0ef3930bc692764721f)
- [i3c_target_callbacks::write_received_cb](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__target__callbacks.html#a7288f143d19ad306616e25e68ffedc03)
- [i3c_target_callbacks::buf_read_requested_cb](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__target__callbacks.html#a9b7ae83ecc4671ea509b4b6f9d01f614)
- [i3c_target_callbacks::buf_write_received_cb](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__target__callbacks.html#abaf52fa6a2189b9e03728a4ae38e66e8)
- [i3c_target_callbacks::read_requested_cb](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__target__callbacks.html#ac72e0bab1eeff6995983f90f6d934749)
- [i3c_target_callbacks::write_requested_cb](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__target__callbacks.html#ad9e51587a8f86f08d065071d28241ee2)
- [i3c_target_callbacks::read_processed_cb](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__target__callbacks.html#ae53661cfa98a3b58a9702fef28234c30)
- [i3c_target_config::callbacks](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__target__config.html#a43ed9a3679d54f7bb91dade34a5897b6)
- [i3c_target_driver_api::driver_register](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__target__driver__api.html#a1d1d0426a197b77a5ddc74ffb670b43c)
- [i3c_target_driver_api::driver_unregister](https://docs.zephyrproject.org/latest/doxygen/html/structi3c__target__driver__api.html#ac933f20f1f8affd685f5958c681648c2)

---

[上一章](P853_system.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P855_tc_capture.h_源码浏览.md)
