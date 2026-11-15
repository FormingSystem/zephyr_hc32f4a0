---
id: learning.zephyr-docs.api-source-device-reference.page-7
title: bluetooth.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2bluetooth_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_bluetooth.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2bluetooth_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2bluetooth_8h.html)。

## 7.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00008"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
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
<a id="foldopen00046"></a>
<a id="l00046"></a>
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
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="foldopen00079"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="foldopen00081"></a>
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
<a id="foldopen00105"></a>
<a id="l00105"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="foldopen00115"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00127"></a>
<a id="foldopen00128"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00135"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="foldopen00151"></a>
<a id="l00151"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="foldopen00217"></a>
<a id="l00217"></a>
<a id="l00221"></a>
<a id="l00225"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00243"></a>
<a id="foldopen00262"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="foldopen00282"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="foldopen00319"></a>
<a id="l00319"></a>
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
<a id="l00332"></a>
<a id="l00333"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="l00337"></a>
<a id="foldopen00350"></a>
<a id="l00350"></a>
<a id="l00351"></a>
<a id="l00352"></a>
<a id="l00353"></a>
<a id="l00354"></a>
<a id="foldopen00376"></a>
<a id="l00376"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="l00380"></a>
<a id="l00381"></a>
<a id="l00382"></a>
<a id="l00383"></a>
<a id="l00384"></a>
<a id="l00385"></a>
<a id="l00386"></a>
<a id="l00387"></a>
<a id="l00388"></a>
<a id="l00389"></a>
<a id="l00390"></a>
<a id="l00391"></a>
<a id="l00392"></a>
<a id="foldopen00420"></a>
<a id="l00420"></a>
<a id="l00421"></a>
<a id="l00422"></a>
<a id="l00423"></a>
<a id="l00424"></a>
<a id="l00425"></a>
<a id="foldopen00441"></a>
<a id="l00441"></a>
<a id="l00442"></a>
<a id="l00443"></a>
<a id="l00444"></a>
<a id="l00445"></a>
<a id="l00446"></a>
<a id="l00447"></a>
<a id="l00448"></a>
<a id="l00449"></a>
<a id="l00450"></a>
<a id="l00451"></a>
<a id="l00452"></a>
<a id="l00471"></a>
<a id="l00472"></a>
<a id="l00500"></a>
<a id="l00501"></a>
<a id="l00505"></a>
<a id="l00506"></a>
<a id="l00507"></a>
<a id="l00508"></a>
<a id="l00509"></a>
<a id="l00521"></a>
<a id="l00522"></a>
<a id="l00534"></a>
<a id="l00535"></a>
<a id="l00547"></a>
<a id="l00548"></a>
<a id="l00561"></a>
<a id="l00562"></a>
<a id="l00575"></a>
<a id="l00576"></a>
<a id="l00577"></a>
<a id="l00578"></a>
<a id="l00579"></a>
<a id="l00580"></a>
<a id="l00581"></a>
<a id="aaddr_8h_html"></a>
<a id="abuf_8h_html"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="adrivers_2bluetooth_8h_html_a362df79e2f782159f7e85d63817421bb"></a>
<a id="adrivers_2bluetooth_8h_html_a8ab7dc7d38f3bc7be72e34d7a9f14212"></a>
<a id="adrivers_2bluetooth_8h_html_ab6b790e6dd0e8251d6cf10b0a7cce5f7"></a>
<a id="adrivers_2bluetooth_8h_html_add813c1343955a7bb95135eb0fbe9cd5"></a>
<a id="adrivers_2bluetooth_8h_html_ae29dbf165252ddf9085c7387706fd09c"></a>
<a id="agroup__bt__hci__api__backend_html_ga29f6af67c9ba45d0945c6de1424ea617"></a>
<a id="agroup__bt__hci__api__backend_html_ga79b12569871b2b6c8420c245e9505aed"></a>
<a id="agroup__bt__hci__api__backend_html_ga93b2a7f403463aa7a1eaf94d7f17c01c"></a>
<a id="agroup__bt__hci__api__backend_html_gaa3205fd69fa1e7f00ea94a492fa9140f"></a>
<a id="agroup__bt__hci__api__backend_html_gad45ae0f5e6f085f7a787257f1315df86"></a>
<a id="agroup__bt__hci__api_html_ga407beb20238b8fe6fdbd4ef199eb1f6c"></a>
<a id="agroup__bt__hci__api_html_ga45ce7bf5fe86f5fff3d8838d247b1d47"></a>
<a id="agroup__bt__hci__api_html_ga4baab0790149536873e5d9e0cb14359f"></a>
<a id="agroup__bt__hci__api_html_ga64079b6f03479561c1c7d09b3af81ede"></a>
<a id="agroup__bt__hci__api_html_ga9df830679cdec440f96e37b608c7fdf7"></a>
<a id="agroup__bt__hci__api_html_gaad2dc7f911913468a1440fad91cb3d62"></a>
<a id="agroup__bt__hci__api_html_gac744c98801cea5afd13d6774154e71c8"></a>
<a id="agroup__bt__hci__api_html_gad187f0aff959a4756b281aa33d1b4394"></a>
<a id="agroup__bt__hci__api_html_gaf2f4e86132f321c6c7f20965dd5c1f0d"></a>
<a id="agroup__bt__hci__api_html_gga687e88a53cddde1d7cbf3057678e66c5a7b850d8c910608f408feb2841f582eea"></a>
<a id="agroup__bt__hci__api_html_gga687e88a53cddde1d7cbf3057678e66c5a8ae71e8530f0aedbc107d38ca09b3ff2"></a>
<a id="agroup__bt__hci__api_html_gga687e88a53cddde1d7cbf3057678e66c5ae6ea7b95de2c304ceafbf7a02373a0c1"></a>
<a id="agroup__net__buf_html_gabedcb728bc2fc0c2b5319a8fd87e8273"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="agroup__system__errno_html_ga43785b9969e0bd1af532dbde06c5540b"></a>
<a id="agroup__system__errno_html_gaa4ccb54aa806de3e41a8515f06db85d4"></a>
<a id="agroup__system__errno_html_gaf23e48762a0676f49d480db91cfd5e4b"></a>
<a id="ahci__vs_8h_html"></a>
<a id="anet__buf_8h_html"></a>
<a id="aposix_2sys_2socket_8h_html_adee01662b0cf762a014efd87ab811276"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructbt__addr__t_html"></a>
<a id="astructbt__hci__driver__api_html"></a>
<a id="astructbt__hci__driver__api_html_a03aecef9fea90013ffe2ca5df63a5b2f"></a>
<a id="astructbt__hci__driver__api_html_a3e87eb7758c2782f024cee1421ebd1fc"></a>
<a id="astructbt__hci__driver__api_html_a889d9a3553c4dd04595198dcfaf61d23"></a>
<a id="astructbt__hci__driver__api_html_acc2ac1f8ec536465eae4500fe972f3af"></a>
<a id="astructbt__hci__driver__config_html"></a>
<a id="astructbt__hci__driver__config_html_a686f78df305033c3d093958e1c374a85"></a>
<a id="astructbt__hci__driver__data_html"></a>
<a id="astructbt__hci__driver__data_html_a60b09de82502158b7e09d6850d2c1ec3"></a>
<a id="astructbt__hci__driver__data_html_a7213640520b14fc3368e1d7354370d93"></a>
<a id="astructbt__hci__setup__params_html"></a>
<a id="astructbt__hci__setup__params_html_a6aea62826eeab39e6af40f9005548f3f"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_a27573cbd10ee145f8bb1396242b27a3e"></a>
<a id="astructnet__buf_html"></a>
<a id="astructnet__buf_html_ae75b7ca728fb7440ea483be8bf88bc38"></a>

```c



#ifndef ZEPHYR_INCLUDE_DRIVERS_BLUETOOTH_H_
#define ZEPHYR_INCLUDE_DRIVERS_BLUETOOTH_H_


#include <stdbool.h>
#include <stdint.h>
#include <zephyr/net_buf.h>
#include <zephyr/bluetooth/buf.h>
#include <zephyr/bluetooth/addr.h>
#include <zephyr/bluetooth/hci_vs.h>
#include <zephyr/device.h>

#ifdef __cplusplus
extern "C" {
#endif

struct bt_hci_setup_params {
        bt_addr_t public_addr;
};

enum {
        /* The host should never send HCI_Reset */
        BT_HCI_QUIRK_NO_RESET = BIT(0),
        /* The controller does not auto-initiate a DLE procedure when the
         * initial connection data length parameters are not equal to the
         * default data length parameters. Therefore the host should initiate
         * the DLE procedure after connection establishment.
         *
         * That requirement is stated in Core Spec v5.4 Vol 6 Part B. 4.5.10
         * Data PDU length management:
         *
         * > For a new connection:
         * > - ... If either value is not 27, then the Controller should
         * >   initiate the Data Length Update procedure at the earliest
         * >   practical opportunity.
         */
        BT_HCI_QUIRK_NO_AUTO_DLE = BIT(1),
        BT_HCI_QUIRK_NO_FLOW_CONTROL = BIT(2),
};

#define BT_DT_HCI_QUIRK_OR(node_id, prop, idx) \
        UTIL_CAT(BT_HCI_QUIRK_, DT_STRING_UPPER_TOKEN_BY_IDX(node_id, prop, idx))
#define BT_DT_HCI_QUIRKS_GET(node_id) COND_CODE_1(DT_NODE_HAS_PROP(node_id, bt_hci_quirks), \
                                                  (DT_FOREACH_PROP_ELEM_SEP(node_id, \
                                                                            bt_hci_quirks, \
                                                                            BT_DT_HCI_QUIRK_OR, \
                                                                            (|))), \
                                                  (0))
#define BT_DT_HCI_QUIRKS_INST_GET(inst) BT_DT_HCI_QUIRKS_GET(DT_DRV_INST(inst))

#define BT_DT_HCI_NAME_GET(node_id) DT_PROP_OR(node_id, bt_hci_name, "HCI")
#define BT_DT_HCI_NAME_INST_GET(inst) BT_DT_HCI_NAME_GET(DT_DRV_INST(inst))

/* Fallback default when there's no property, same as "virtual" */
#define BT_PRIV_HCI_BUS_DEFAULT (0)
#define BT_DT_HCI_BUS_GET(node_id) DT_ENUM_IDX_OR(node_id, bt_hci_bus, BT_PRIV_HCI_BUS_DEFAULT)

#define BT_DT_HCI_BUS_INST_GET(inst) BT_DT_HCI_BUS_GET(DT_DRV_INST(inst))

struct bt_hci_driver_config {
        uint32_t quirks;
};

#define BT_DT_HCI_DRIVER_CONFIG_GET(node_id)                                                    \
        {                                                                                       \
                .quirks = (uint32_t)BT_DT_HCI_QUIRKS_GET(node_id),                                \
        }


#define BT_DT_HCI_DRIVER_CONFIG_INST_GET(inst)                                                  \
        BT_DT_HCI_DRIVER_CONFIG_GET(DT_DRV_INST(inst))


typedef int (*bt_hci_recv_t)(const struct device *dev, struct net_buf *buf);

struct bt_hci_driver_data {
        bt_hci_recv_t recv;
#if defined(CONFIG_BT_HCI_SET_PUBLIC_ADDR) || defined(__DOXYGEN__)
        bt_addr_t public_addr;
#endif /* CONFIG_BT_HCI_SET_PUBLIC_ADDR */
};

typedef int (*bt_hci_api_open_t)(const struct device *dev);

typedef int (*bt_hci_api_close_t)(const struct device *dev);

typedef int (*bt_hci_api_send_t)(const struct device *dev, struct net_buf *buf);

typedef int (*bt_hci_api_setup_t)(const struct device *dev,
                                  const struct bt_hci_setup_params *param);

__subsystem struct bt_hci_driver_api {
        bt_hci_api_open_t open;
        bt_hci_api_close_t close;
        bt_hci_api_send_t send;
#if defined(CONFIG_BT_HCI_SETUP) || defined(__DOXYGEN__)
        bt_hci_api_setup_t setup;
#endif /* CONFIG_BT_HCI_SETUP */
};


static inline int bt_hci_recv_err(const struct device *dev, struct net_buf *buf)
{
        struct bt_hci_driver_data *data = dev->data;

        if (data->recv == NULL) {
                return -ENOTCONN;
        }

        return data->recv(dev, buf);
}

static inline void bt_hci_recv(const struct device *dev, struct net_buf *buf)
{
        int err;

        err = bt_hci_recv_err(dev, buf);
        if (err != 0) {
                net_buf_unref(buf);
        }
}

static inline int bt_hci_open(const struct device *dev, bt_hci_recv_t recv)
{
        struct bt_hci_driver_data *data = dev->data;
        int err;

        if (data->recv != NULL) {
                return -EALREADY;
        }

        data->recv = recv;

        err = DEVICE_API_GET(bt_hci, dev)->open(dev);
        if (err != 0) {
                data->recv = NULL;
        }

        return err;
}

static inline bool bt_hci_can_close(const struct device *dev)
{
        return DEVICE_API_GET(bt_hci, dev)->close != NULL;
}

static inline int bt_hci_close(const struct device *dev)
{
        struct bt_hci_driver_data *data = dev->data;
        int err = 0;

        if (!bt_hci_can_close(dev)) {
                return -ENOSYS;
        }

        err = DEVICE_API_GET(bt_hci, dev)->close(dev);
        if (err == 0) {
                data->recv = NULL;
        }

        return err;
}

static inline int bt_hci_send(const struct device *dev, struct net_buf *buf)
{
        return DEVICE_API_GET(bt_hci, dev)->send(dev, buf);
}

#if defined(CONFIG_BT_HCI_SETUP) || defined(__DOXYGEN__)
static inline int bt_hci_setup(const struct device *dev, struct bt_hci_setup_params *params)
{
        const struct bt_hci_driver_api *api = DEVICE_API_GET(bt_hci, dev);

        if (api->setup == NULL) {
                return -ENOSYS;
        }

        return api->setup(dev, params);
}
#endif

void bt_hci_set_public_addr(const struct device *dev, const bt_addr_t *addr);

const bt_addr_t *bt_hci_get_public_addr(const struct device *dev);


/* The following functions are not strictly part of the HCI driver API, in that
 * they do not take as input a struct device which implements the HCI driver API.
 */

int bt_hci_transport_setup(const struct device *dev);

int bt_hci_transport_teardown(const struct device *dev);

struct net_buf *bt_hci_evt_create(uint8_t evt, uint8_t len);

struct net_buf *bt_hci_cmd_complete_create(uint16_t op, uint8_t plen);

struct net_buf *bt_hci_cmd_status_create(uint16_t op, uint8_t status);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_BLUETOOTH_H_ */
```

## 7.2\_可见注释译文（Comments）

### 注释 1：原第 56 行

主机（Host）不应发送 `HCI_Reset`。

### 注释 2：原第 58 行

当初始连接数据长度参数（Initial Connection Data Length Parameters）与默认数据长度参数不一致时，控制器（Controller）不会自动发起数据长度扩展过程（Data Length Extension，DLE）。因此，主机（Host）应在建立连接之后发起 DLE 过程。

该要求见《核心规范》（Core Spec）v5.4 第 6 卷 B 部分 4.5.10“数据协议数据单元长度管理（Data PDU Length Management）”：

> 对于一个新连接：
> - ……如果两个值中的任一个不为 27，控制器就应在实际可行的最早时机发起数据长度更新过程（Data Length Update Procedure）。

### 注释 3：原第 92 行

未提供属性（Property）时的回退默认值（Fallback Default），与 `virtual` 相同。

### 注释 4：原第 167 行

条件编译配置（Configuration）标记：`CONFIG_BT_HCI_SET_PUBLIC_ADDR`。

### 注释 5：原第 238 行

条件编译配置（Configuration）标记：`CONFIG_BT_HCI_SETUP`。

### 注释 6：原第 506 行

严格来说，下列函数不属于主机控制器接口驱动 API（HCI Driver API），因为它们不接收实现该 API 的 `struct device` 作为输入。

### 注释 7：原第 581 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_BLUETOOTH_H_`。

## 7.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2bluetooth_8h.html)
- [stdbool.h](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md)
- [stdint.h](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md)
- [zephyr/net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [zephyr/bluetooth/buf.h](https://docs.zephyrproject.org/latest/doxygen/html/buf_8h.html)
- [zephyr/bluetooth/addr.h](https://docs.zephyrproject.org/latest/doxygen/html/addr_8h.html)
- [zephyr/bluetooth/hci_vs.h](../api_file_runtime_reference/P017_zephyr__bluetooth__hci_vs.h_文件参考.md)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [bt_hci_setup_params](../bluetooth_hci_model_reference/P437_bt_hci_setup_params_结构体.md)
- [bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)
- [public_addr](../bluetooth_hci_model_reference/P437_bt_hci_setup_params_结构体.md#a6aea62826eeab39e6af40f9005548f3f)
- [BT_HCI_QUIRK_NO_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#gga687e88a53cddde1d7cbf3057678e66c5ae6ea7b95de2c304ceafbf7a02373a0c1)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [BT_HCI_QUIRK_NO_AUTO_DLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#gga687e88a53cddde1d7cbf3057678e66c5a8ae71e8530f0aedbc107d38ca09b3ff2)
- [BT_HCI_QUIRK_NO_FLOW_CONTROL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#gga687e88a53cddde1d7cbf3057678e66c5a7b850d8c910608f408feb2841f582eea)
- [bt_hci_driver_config](../bluetooth_hci_model_reference/P201_bt_hci_driver_config_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [quirks](../bluetooth_hci_model_reference/P201_bt_hci_driver_config_结构体.md#a686f78df305033c3d093958e1c374a85)
- [bt_hci_recv_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api__backend.html#ga79b12569871b2b6c8420c245e9505aed)
- [device](../device_reference/P002_设备对象结构.md)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [bt_hci_driver_data](../bluetooth_hci_model_reference/P202_bt_hci_driver_data_结构体.md)
- [recv](../bluetooth_hci_model_reference/P202_bt_hci_driver_data_结构体.md#a7213640520b14fc3368e1d7354370d93)
- [public_addr](../bluetooth_hci_model_reference/P202_bt_hci_driver_data_结构体.md#a60b09de82502158b7e09d6850d2c1ec3)
- [bt_hci_api_open_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api__backend.html#gad45ae0f5e6f085f7a787257f1315df86)
- [bt_hci_api_close_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api__backend.html#ga93b2a7f403463aa7a1eaf94d7f17c01c)
- [bt_hci_api_send_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api__backend.html#ga29f6af67c9ba45d0945c6de1424ea617)
- [bt_hci_api_setup_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api__backend.html#gaa3205fd69fa1e7f00ea94a492fa9140f)
- [bt_hci_driver_api](../bluetooth_hci_model_reference/P200_bt_hci_driver_api_结构体.md)
- [open](../bluetooth_hci_model_reference/P200_bt_hci_driver_api_结构体.md#a889d9a3553c4dd04595198dcfaf61d23)
- [close](../bluetooth_hci_model_reference/P200_bt_hci_driver_api_结构体.md#a03aecef9fea90013ffe2ca5df63a5b2f)
- [send](../bluetooth_hci_model_reference/P200_bt_hci_driver_api_结构体.md#a3e87eb7758c2782f024cee1421ebd1fc)
- [setup](../bluetooth_hci_model_reference/P200_bt_hci_driver_api_结构体.md#acc2ac1f8ec536465eae4500fe972f3af)
- [bt_hci_recv_err](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#gaad2dc7f911913468a1440fad91cb3d62)
- [data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [ENOTCONN](../error_reference/P003_系统错误号公共接口.md#gaf23e48762a0676f49d480db91cfd5e4b)
- [bt_hci_recv](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#ga407beb20238b8fe6fdbd4ef199eb1f6c)
- [net_buf_unref](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gabedcb728bc2fc0c2b5319a8fd87e8273)
- [bt_hci_open](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#gac744c98801cea5afd13d6774154e71c8)
- [recv](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#adee01662b0cf762a014efd87ab811276)
- [EALREADY](../error_reference/P003_系统错误号公共接口.md#gaa4ccb54aa806de3e41a8515f06db85d4)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [bt_hci_can_close](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#ga4baab0790149536873e5d9e0cb14359f)
- [bt_hci_close](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#gad187f0aff959a4756b281aa33d1b4394)
- [ENOSYS](../error_reference/P003_系统错误号公共接口.md#ga43785b9969e0bd1af532dbde06c5540b)
- [bt_hci_send](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#ga64079b6f03479561c1c7d09b3af81ede)
- [bt_hci_setup](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#ga45ce7bf5fe86f5fff3d8838d247b1d47)
- [bt_hci_set_public_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#ga9df830679cdec440f96e37b608c7fdf7)
- [bt_hci_get_public_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html#gaf2f4e86132f321c6c7f20965dd5c1f0d)
- [bt_hci_transport_setup](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2bluetooth_8h.html#add813c1343955a7bb95135eb0fbe9cd5)
- [bt_hci_transport_teardown](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2bluetooth_8h.html#ae29dbf165252ddf9085c7387706fd09c)
- [bt_hci_evt_create](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2bluetooth_8h.html#a362df79e2f782159f7e85d63817421bb)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [len](../network_core_model_reference/P046_net_buf_结构体.md#ae75b7ca728fb7440ea483be8bf88bc38)
- [bt_hci_cmd_complete_create](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2bluetooth_8h.html#a8ab7dc7d38f3bc7be72e34d7a9f14212)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bt_hci_cmd_status_create](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2bluetooth_8h.html#ab6b790e6dd0e8251d6cf10b0a7cce5f7)
- [addr.h](https://docs.zephyrproject.org/latest/doxygen/html/addr_8h.html)
- [buf.h](https://docs.zephyrproject.org/latest/doxygen/html/buf_8h.html)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [hci_vs.h](../api_file_runtime_reference/P017_zephyr__bluetooth__hci_vs.h_文件参考.md)
- [net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [bt_hci_driver_api::close](../bluetooth_hci_model_reference/P200_bt_hci_driver_api_结构体.md#a03aecef9fea90013ffe2ca5df63a5b2f)
- [bt_hci_driver_api::send](../bluetooth_hci_model_reference/P200_bt_hci_driver_api_结构体.md#a3e87eb7758c2782f024cee1421ebd1fc)
- [bt_hci_driver_api::open](../bluetooth_hci_model_reference/P200_bt_hci_driver_api_结构体.md#a889d9a3553c4dd04595198dcfaf61d23)
- [bt_hci_driver_api::setup](../bluetooth_hci_model_reference/P200_bt_hci_driver_api_结构体.md#acc2ac1f8ec536465eae4500fe972f3af)
- [bt_hci_driver_config::quirks](../bluetooth_hci_model_reference/P201_bt_hci_driver_config_结构体.md#a686f78df305033c3d093958e1c374a85)
- [bt_hci_driver_data::public_addr](../bluetooth_hci_model_reference/P202_bt_hci_driver_data_结构体.md#a60b09de82502158b7e09d6850d2c1ec3)
- [bt_hci_driver_data::recv](../bluetooth_hci_model_reference/P202_bt_hci_driver_data_结构体.md#a7213640520b14fc3368e1d7354370d93)
- [bt_hci_setup_params::public_addr](../bluetooth_hci_model_reference/P437_bt_hci_setup_params_结构体.md#a6aea62826eeab39e6af40f9005548f3f)
- [device::data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [net_buf::len](../network_core_model_reference/P046_net_buf_结构体.md#ae75b7ca728fb7440ea483be8bf88bc38)

---

[上一章](P006_demand_paging.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P008_esai.h_源码浏览.md)
