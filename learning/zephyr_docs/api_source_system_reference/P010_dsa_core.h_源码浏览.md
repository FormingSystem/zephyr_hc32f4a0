---
id: learning.zephyr-docs.api-source-system-reference.page-10
title: dsa_core.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dsa__core_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_dsa\_core.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/dsa__core_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../api_file_runtime_reference/P013_zephyr__net__dsa_core.h_文件参考.md)。

## 10.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
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
<a id="l00028"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="foldopen00050"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
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
<a id="foldopen00071"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="foldopen00098"></a>
<a id="l00098"></a>
<a id="l00100"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="foldopen00144"></a>
<a id="l00144"></a>
<a id="l00146"></a>
<a id="l00148"></a>
<a id="l00150"></a>
<a id="l00152"></a>
<a id="l00154"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
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
<a id="l00194"></a>
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
<a id="l00214"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00233"></a>
<a id="adevice_8h_html"></a>
<a id="adevicetree_8h_html"></a>
<a id="aerrno_8h_html"></a>
<a id="aethernet_8h_html"></a>
<a id="agroup__dsa__core_html_ga16d03129d1e4c39f8662dae4b35598d9"></a>
<a id="agroup__ethernet_html_ga9162ff11d626813fc840df0b67820ac5"></a>
<a id="anet__if_8h_html"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="aphy_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructdevice_html"></a>
<a id="astructdsa__api_html"></a>
<a id="astructdsa__api_html_a1893ae289acf61ce96d9ad9bb11f43d9"></a>
<a id="astructdsa__api_html_a3ad664182c5cee8786600d4dcd9bae1a"></a>
<a id="astructdsa__api_html_a5117a72ebe047a23f18e168282b74a30"></a>
<a id="astructdsa__api_html_a7d0809973c38681d5e35613ce999fa1c"></a>
<a id="astructdsa__api_html_aa72473bfb8a85f95f4d3b56cd87e7257"></a>
<a id="astructdsa__api_html_aca5e37c3e5a441ddca1403ac733e011d"></a>
<a id="astructdsa__api_html_ae93ff737cfc6f911e0972b28988f8d1b"></a>
<a id="astructdsa__api_html_ae941da97713f1e3511c03509b1f2386f"></a>
<a id="astructdsa__port__config_html"></a>
<a id="astructdsa__port__config_html_a22b68800b01f9b886949f50b6976ce93"></a>
<a id="astructdsa__port__config_html_a3ab024894788e956b545d6b3114e8739"></a>
<a id="astructdsa__port__config_html_a521f8ad8298fce309f80785b850f6eef"></a>
<a id="astructdsa__port__config_html_a7c4578af241d554b0e8b253542c9deb6"></a>
<a id="astructdsa__port__config_html_a8eac549c19d9f9999b95c95fa112ff97"></a>
<a id="astructdsa__port__config_html_a97138eca5243d1564badfe89fd04bbd4"></a>
<a id="astructdsa__port__config_html_a997a4268a7aed1cc4b790d8da39c5cad"></a>
<a id="astructdsa__port__config_html_acebba6797230c65baac4403b578e1cbb"></a>
<a id="astructdsa__switch__context_html"></a>
<a id="astructdsa__switch__context_html_a0961bfc0c6ba7047328210245322a9d7"></a>
<a id="astructdsa__switch__context_html_a0eb8ee97a922eaefdaed00cf75ec5a26"></a>
<a id="astructdsa__switch__context_html_a227551d262998fb83dcd06ebfccdb4d7"></a>
<a id="astructdsa__switch__context_html_a4ca4e815b96c29cb26aef7ff02d8b03c"></a>
<a id="astructdsa__switch__context_html_a68a619b3db141ba6127ccc4577f2edf5"></a>
<a id="astructdsa__switch__context_html_ad6670b8743639c7837b9188a9e8a70eb"></a>
<a id="astructdsa__switch__context_html_ae9437d8ef21a64cdb297623096cd77f3"></a>
<a id="astructethernet__api_html"></a>
<a id="astructnet__eth__mac__config_html"></a>
<a id="astructnet__if_html"></a>
<a id="astructnet__pkt_html"></a>
<a id="astructphy__link__state_html"></a>

```c
/*
 * Copyright 2025 NXP
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_DSA_CORE_H_
#define ZEPHYR_INCLUDE_NET_DSA_CORE_H_

#include <errno.h>
#include <zephyr/device.h>
#include <zephyr/devicetree.h>
#include <zephyr/net/net_if.h>
#include <zephyr/net/phy.h>
#include <zephyr/net/ethernet.h>



#if defined(CONFIG_DSA_PORT_MAX_COUNT)
#define DSA_PORT_MAX_COUNT CONFIG_DSA_PORT_MAX_COUNT
#else
#define DSA_PORT_MAX_COUNT 0
#endif


#ifdef __cplusplus
extern "C" {
#endif

#define DSA_PORT_INST_INIT(port, n, cfg)                                                           \
        ETH_NET_DEVICE_DT_DEFINE(port, dsa_port_initialize, NULL, &dsa_switch_context_##n, cfg,    \
                                 CONFIG_ETH_INIT_PRIORITY, &dsa_eth_api, NET_ETH_MTU)

#define DSA_SWITCH_INST_INIT(n, _dapi, data, fn)                                                   \
        struct dsa_switch_context dsa_switch_context_##n = {                                       \
                .dapi = _dapi,                                                                     \
                .prv_data = data,                                                                  \
                .init_ports = 0,                                                                   \
                .num_ports = DT_INST_CHILD_NUM_STATUS_OKAY(n),                                     \
        };                                                                                         \
        DT_INST_FOREACH_CHILD_STATUS_OKAY_VARGS(n, fn, n);

struct dsa_switch_context {
        struct net_if *iface_user[DSA_PORT_MAX_COUNT];

        struct net_if *iface_conduit;

        struct dsa_api *dapi;

        void *prv_data;

        uint8_t num_ports;

        uint8_t init_ports;

        void *tagger_data;
};

struct dsa_api {

        struct net_if *(*recv)(struct net_if *iface, struct net_pkt *pkt);

        struct net_pkt *(*xmit)(struct net_if *iface, struct net_pkt *pkt);

        int (*port_init)(const struct device *dev);

        void (*port_phylink_change)(const struct device *phy_dev, struct phy_link_state *state,
                                    const struct device *dev);

#if defined(CONFIG_NET_L2_PTP_TIMESTAMPING) || defined(__DOXYGEN__)
        int (*port_txtstamp)(const struct device *dev, struct net_pkt *pkt);
#endif
        int (*switch_setup)(const struct dsa_switch_context *dsa_switch_ctx);

        int (*connect_tag_protocol)(struct dsa_switch_context *dsa_switch_ctx, int tag_proto);

        enum ethernet_hw_caps (*get_capabilities)(const struct device *dev);

        int (*set_config)(const struct device *dev,
                          enum ethernet_config_type type,
                          const struct ethernet_config *config);

        int (*get_config)(const struct device *dev,
                          enum ethernet_config_type type,
                          struct ethernet_config *config);
};

struct dsa_port_config {
        struct net_eth_mac_config mcfg;
        const int port_idx;
        const struct device *phy_dev;
        const char *phy_mode;
        const int tag_proto;
        const struct device *ethernet_connection;
#if defined(CONFIG_NET_L2_PTP_TIMESTAMPING) || defined(__DOXYGEN__)
        const struct device *ptp_clock;
#endif
        void *prv_config;
};


/*
 * DSA port init
 *
 * Returns:
 *  - 0 if ok, < 0 if error
 */
int dsa_port_initialize(const struct device *dev);

/*
 * DSA transmit function
 *
 * param dev: Port device to transmit
 * param pkt: Network packet
 *
 * Returns:
 *  - 0 if ok, < 0 if error
 */
int dsa_xmit(const struct device *dev, struct net_pkt *pkt);

/*
 * DSA receive function
 *
 * param iface: Interface of conduit port
 * param pkt: Network packet
 *
 * Returns:
 *  - Interface to redirect
 */
struct net_if *dsa_recv(struct net_if *iface, struct net_pkt *pkt);

/*
 * DSA ethernet init function to handle flags
 *
 * param iface: Interface of port
 *
 * Returns:
 *  - 0 if ok, < 0 if error
 */
int dsa_eth_init(struct net_if *iface);

/* Ethernet APIs definition for switch ports */
extern const struct ethernet_api dsa_eth_api;


struct net_if *dsa_user_get_iface(struct net_if *iface, int port_idx);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_NET_DSA_CORE_H_ */
```

## 10.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2025 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 170 行

分布式交换架构端口初始化（DSA Port Init）。

返回（Returns）：成功时为 0，错误时小于 0。

### 注释 3：原第 178 行

分布式交换架构发送函数（DSA Transmit Function）。

参数 `dev`：执行发送的端口设备（Port Device）。
参数 `pkt`：网络数据包（Network Packet）。

返回（Returns）：成功时为 0，错误时小于 0。

### 注释 4：原第 189 行

分布式交换架构接收函数（DSA Receive Function）。

参数 `iface`：主通道端口（Conduit Port）的接口。
参数 `pkt`：网络数据包（Network Packet）。

返回（Returns）：重定向目标接口（Interface to Redirect）。

### 注释 5：原第 200 行

用于处理标志（Flags）的分布式交换架构以太网初始化函数（DSA Ethernet Init Function）。

参数 `iface`：端口接口（Interface of Port）。

返回（Returns）：成功时为 0，错误时小于 0。

### 注释 6：原第 210 行

交换机端口（Switch Ports）的以太网 API 定义（Ethernet APIs Definition）。

### 注释 7：原第 233 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_DSA_CORE_H_`。

## 10.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../api_file_runtime_reference/P013_zephyr__net__dsa_core.h_文件参考.md)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [zephyr/net/net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [zephyr/net/phy.h](https://docs.zephyrproject.org/latest/doxygen/html/phy_8h.html)
- [zephyr/net/ethernet.h](https://docs.zephyrproject.org/latest/doxygen/html/ethernet_8h.html)
- [dsa_switch_context](../network_service_model_reference/P004_dsa_switch_context_结构体.md)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [iface_user](../network_service_model_reference/P004_dsa_switch_context_结构体.md#ad6670b8743639c7837b9188a9e8a70eb)
- [iface_conduit](../network_service_model_reference/P004_dsa_switch_context_结构体.md#a227551d262998fb83dcd06ebfccdb4d7)
- [dsa_api](../network_service_model_reference/P002_dsa_api_结构体.md)
- [dapi](../network_service_model_reference/P004_dsa_switch_context_结构体.md#a4ca4e815b96c29cb26aef7ff02d8b03c)
- [prv_data](../network_service_model_reference/P004_dsa_switch_context_结构体.md#a0eb8ee97a922eaefdaed00cf75ec5a26)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [num_ports](../network_service_model_reference/P004_dsa_switch_context_结构体.md#ae9437d8ef21a64cdb297623096cd77f3)
- [init_ports](../network_service_model_reference/P004_dsa_switch_context_结构体.md#a68a619b3db141ba6127ccc4577f2edf5)
- [tagger_data](../network_service_model_reference/P004_dsa_switch_context_结构体.md#a0961bfc0c6ba7047328210245322a9d7)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)
- [port_init](../network_service_model_reference/P002_dsa_api_结构体.md#a5117a72ebe047a23f18e168282b74a30)
- [device](../device_reference/P002_设备对象结构.md)
- [port_phylink_change](../network_service_model_reference/P002_dsa_api_结构体.md#ae93ff737cfc6f911e0972b28988f8d1b)
- [phy_link_state](../network_service_model_reference/P040_phy_link_state_结构体.md)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [port_txtstamp](../network_service_model_reference/P002_dsa_api_结构体.md#aca5e37c3e5a441ddca1403ac733e011d)
- [switch_setup](../network_service_model_reference/P002_dsa_api_结构体.md#a3ad664182c5cee8786600d4dcd9bae1a)
- [connect_tag_protocol](../network_service_model_reference/P002_dsa_api_结构体.md#aa72473bfb8a85f95f4d3b56cd87e7257)
- [ethernet_hw_caps](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html#ga9162ff11d626813fc840df0b67820ac5)
- [get_capabilities](../network_service_model_reference/P002_dsa_api_结构体.md#a7d0809973c38681d5e35613ce999fa1c)
- [set_config](../network_service_model_reference/P002_dsa_api_结构体.md#ae941da97713f1e3511c03509b1f2386f)
- [get_config](../network_service_model_reference/P002_dsa_api_结构体.md#a1893ae289acf61ce96d9ad9bb11f43d9)
- [dsa_port_config](../network_service_model_reference/P003_dsa_port_config_结构体.md)
- [net_eth_mac_config](../network_core_model_reference/P060_net_eth_mac_config_结构体.md)
- [mcfg](../network_service_model_reference/P003_dsa_port_config_结构体.md#a997a4268a7aed1cc4b790d8da39c5cad)
- [port_idx](../network_service_model_reference/P003_dsa_port_config_结构体.md#a521f8ad8298fce309f80785b850f6eef)
- [phy_dev](../network_service_model_reference/P003_dsa_port_config_结构体.md#acebba6797230c65baac4403b578e1cbb)
- [phy_mode](../network_service_model_reference/P003_dsa_port_config_结构体.md#a8eac549c19d9f9999b95c95fa112ff97)
- [tag_proto](../network_service_model_reference/P003_dsa_port_config_结构体.md#a7c4578af241d554b0e8b253542c9deb6)
- [ethernet_connection](../network_service_model_reference/P003_dsa_port_config_结构体.md#a97138eca5243d1564badfe89fd04bbd4)
- [ptp_clock](../network_service_model_reference/P003_dsa_port_config_结构体.md#a22b68800b01f9b886949f50b6976ce93)
- [prv_config](../network_service_model_reference/P003_dsa_port_config_结构体.md#a3ab024894788e956b545d6b3114e8739)
- [ethernet_api](../network_service_model_reference/P007_ethernet_api_结构体.md)
- [dsa_user_get_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__dsa__core.html#ga16d03129d1e4c39f8662dae4b35598d9)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [ethernet.h](https://docs.zephyrproject.org/latest/doxygen/html/ethernet_8h.html)
- [net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [phy.h](https://docs.zephyrproject.org/latest/doxygen/html/phy_8h.html)
- [dsa_api::get_config](../network_service_model_reference/P002_dsa_api_结构体.md#a1893ae289acf61ce96d9ad9bb11f43d9)
- [dsa_api::switch_setup](../network_service_model_reference/P002_dsa_api_结构体.md#a3ad664182c5cee8786600d4dcd9bae1a)
- [dsa_api::port_init](../network_service_model_reference/P002_dsa_api_结构体.md#a5117a72ebe047a23f18e168282b74a30)
- [dsa_api::get_capabilities](../network_service_model_reference/P002_dsa_api_结构体.md#a7d0809973c38681d5e35613ce999fa1c)
- [dsa_api::connect_tag_protocol](../network_service_model_reference/P002_dsa_api_结构体.md#aa72473bfb8a85f95f4d3b56cd87e7257)
- [dsa_api::port_txtstamp](../network_service_model_reference/P002_dsa_api_结构体.md#aca5e37c3e5a441ddca1403ac733e011d)
- [dsa_api::port_phylink_change](../network_service_model_reference/P002_dsa_api_结构体.md#ae93ff737cfc6f911e0972b28988f8d1b)
- [dsa_api::set_config](../network_service_model_reference/P002_dsa_api_结构体.md#ae941da97713f1e3511c03509b1f2386f)
- [dsa_port_config::ptp_clock](../network_service_model_reference/P003_dsa_port_config_结构体.md#a22b68800b01f9b886949f50b6976ce93)
- [dsa_port_config::prv_config](../network_service_model_reference/P003_dsa_port_config_结构体.md#a3ab024894788e956b545d6b3114e8739)
- [dsa_port_config::port_idx](../network_service_model_reference/P003_dsa_port_config_结构体.md#a521f8ad8298fce309f80785b850f6eef)
- [dsa_port_config::tag_proto](../network_service_model_reference/P003_dsa_port_config_结构体.md#a7c4578af241d554b0e8b253542c9deb6)
- [dsa_port_config::phy_mode](../network_service_model_reference/P003_dsa_port_config_结构体.md#a8eac549c19d9f9999b95c95fa112ff97)
- [dsa_port_config::ethernet_connection](../network_service_model_reference/P003_dsa_port_config_结构体.md#a97138eca5243d1564badfe89fd04bbd4)
- [dsa_port_config::mcfg](../network_service_model_reference/P003_dsa_port_config_结构体.md#a997a4268a7aed1cc4b790d8da39c5cad)
- [dsa_port_config::phy_dev](../network_service_model_reference/P003_dsa_port_config_结构体.md#acebba6797230c65baac4403b578e1cbb)
- [dsa_switch_context::tagger_data](../network_service_model_reference/P004_dsa_switch_context_结构体.md#a0961bfc0c6ba7047328210245322a9d7)
- [dsa_switch_context::prv_data](../network_service_model_reference/P004_dsa_switch_context_结构体.md#a0eb8ee97a922eaefdaed00cf75ec5a26)
- [dsa_switch_context::iface_conduit](../network_service_model_reference/P004_dsa_switch_context_结构体.md#a227551d262998fb83dcd06ebfccdb4d7)
- [dsa_switch_context::dapi](../network_service_model_reference/P004_dsa_switch_context_结构体.md#a4ca4e815b96c29cb26aef7ff02d8b03c)
- [dsa_switch_context::init_ports](../network_service_model_reference/P004_dsa_switch_context_结构体.md#a68a619b3db141ba6127ccc4577f2edf5)
- [dsa_switch_context::iface_user](../network_service_model_reference/P004_dsa_switch_context_结构体.md#ad6670b8743639c7837b9188a9e8a70eb)
- [dsa_switch_context::num_ports](../network_service_model_reference/P004_dsa_switch_context_结构体.md#ae9437d8ef21a64cdb297623096cd77f3)

---

[上一章](P009_util.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P011_eth_nxp_enet.h_源码浏览.md)
