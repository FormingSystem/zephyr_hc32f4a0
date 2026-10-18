---
id: learning.zephyr-docs.api-source-reference.page-18
title: aics.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/aics_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_aics.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/aics_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/aics_8h.html)。

## 18.1\_原始可见代码（Source Code）

<a id="l00001"></a>
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
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00066"></a>
<a id="l00072"></a>
<a id="l00078"></a>
<a id="l00084"></a>
<a id="l00086"></a>
<a id="foldopen00094"></a>
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
<a id="l00115"></a>
<a id="l00117"></a>
<a id="l00119"></a>
<a id="l00121"></a>
<a id="l00123"></a>
<a id="l00125"></a>
<a id="l00127"></a>
<a id="l00129"></a>
<a id="l00131"></a>
<a id="l00140"></a>
<a id="l00142"></a>
<a id="l00144"></a>
<a id="l00146"></a>
<a id="l00148"></a>
<a id="l00150"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="foldopen00158"></a>
<a id="l00158"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="foldopen00194"></a>
<a id="l00194"></a>
<a id="l00200"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="l00334"></a>
<a id="l00346"></a>
<a id="l00347"></a>
<a id="foldopen00353"></a>
<a id="l00353"></a>
<a id="l00355"></a>
<a id="l00357"></a>
<a id="l00359"></a>
<a id="l00361"></a>
<a id="l00363"></a>
<a id="l00364"></a>
<a id="l00365"></a>
<a id="l00367"></a>
<a id="l00369"></a>
<a id="l00371"></a>
<a id="l00373"></a>
<a id="l00375"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="l00380"></a>
<a id="l00381"></a>
<a id="l00394"></a>
<a id="l00395"></a>
<a id="l00396"></a>
<a id="l00407"></a>
<a id="l00408"></a>
<a id="l00420"></a>
<a id="l00421"></a>
<a id="l00429"></a>
<a id="l00430"></a>
<a id="l00438"></a>
<a id="l00439"></a>
<a id="l00447"></a>
<a id="l00448"></a>
<a id="l00456"></a>
<a id="l00457"></a>
<a id="l00468"></a>
<a id="l00469"></a>
<a id="l00477"></a>
<a id="l00478"></a>
<a id="l00486"></a>
<a id="l00487"></a>
<a id="l00495"></a>
<a id="l00496"></a>
<a id="l00507"></a>
<a id="l00508"></a>
<a id="l00516"></a>
<a id="l00517"></a>
<a id="l00525"></a>
<a id="l00526"></a>
<a id="l00536"></a>
<a id="l00537"></a>
<a id="l00545"></a>
<a id="l00546"></a>
<a id="l00555"></a>
<a id="l00556"></a>
<a id="l00562"></a>
<a id="l00563"></a>
<a id="l00574"></a>
<a id="l00575"></a>
<a id="l00582"></a>
<a id="l00583"></a>
<a id="l00584"></a>
<a id="l00585"></a>
<a id="l00586"></a>
<a id="l00587"></a>
<a id="l00591"></a>
<a id="l00592"></a>
<a id="abluetooth_2bluetooth_8h_html"></a>
<a id="agroup__bt__aics_html_ga008ef5cebfcb9b4a3084f411fa81238e"></a>
<a id="agroup__bt__aics_html_ga044d92a4273c6537a9cdf20922352ed6"></a>
<a id="agroup__bt__aics_html_ga0460e82d4277a2c4b14964799ad5f2b0"></a>
<a id="agroup__bt__aics_html_ga0ac3a583dd7ca58a0d356d9f60797517"></a>
<a id="agroup__bt__aics_html_ga0e088e26cf73f1f3b918660d4acdebb9"></a>
<a id="agroup__bt__aics_html_ga11da08c010f4aa849c2e3725dc5cbaeb"></a>
<a id="agroup__bt__aics_html_ga20f3a178788ec6aef593034159793b94"></a>
<a id="agroup__bt__aics_html_ga22869d8a62eb59bc4aad25946da8f9cf"></a>
<a id="agroup__bt__aics_html_ga23bbc1393d21fe38f501813935b25b3d"></a>
<a id="agroup__bt__aics_html_ga2e851f49f9c7e71a18376468a13fdf4f"></a>
<a id="agroup__bt__aics_html_ga36991fe1dee5168db618518d094d80ef"></a>
<a id="agroup__bt__aics_html_ga38d7131397d7762d3bd53e152a6c6130"></a>
<a id="agroup__bt__aics_html_ga43396d2d4b3bd9cdd0c82275fafeadfc"></a>
<a id="agroup__bt__aics_html_ga4be4c4e3c74aa55fbf599157aa1c2098"></a>
<a id="agroup__bt__aics_html_ga4d511e81dd0f0a72fd502bc05dd85e91"></a>
<a id="agroup__bt__aics_html_ga5345254eaf099560e609d97044b39a97"></a>
<a id="agroup__bt__aics_html_ga5a1ad98afe45da9ffbb7247671385d40"></a>
<a id="agroup__bt__aics_html_ga6b536bdcab602ccaccfafe3b37258890"></a>
<a id="agroup__bt__aics_html_ga6e76b9f2de4cdbcd7539c76f6a347fa5"></a>
<a id="agroup__bt__aics_html_ga759712886cd3c4c025ea360dcb663c59"></a>
<a id="agroup__bt__aics_html_ga7cf0508dd7407ec3bb92dec71cc00816"></a>
<a id="agroup__bt__aics_html_ga7ddb93125f6275fc7c99fbf448e24f0c"></a>
<a id="agroup__bt__aics_html_ga7de5ffd2eb61ca562b9773b37470ebd9"></a>
<a id="agroup__bt__aics_html_ga8b415343e7ecf399ecfd0dcaa49bd1ee"></a>
<a id="agroup__bt__aics_html_ga913838aa0d5bff239c2faef4d8a8b36b"></a>
<a id="agroup__bt__aics_html_ga98b142ea7a66de5577c44aa90d507930"></a>
<a id="agroup__bt__aics_html_ga9fda39f8410308e05eb928eeb7267e83"></a>
<a id="agroup__bt__aics_html_gab10ad3599f5b602cdf5504bc92508109"></a>
<a id="agroup__bt__aics_html_gab660d2d4603de3837a3b93ce11e4d0fd"></a>
<a id="agroup__bt__aics_html_gabd6bdcdad0dd5a4c509f9e7cabb3e601"></a>
<a id="agroup__bt__aics_html_gac46268949fa7cbbb827d149a3a904daa"></a>
<a id="agroup__bt__aics_html_gad16d296462af2f61a893bda8d25cc9de"></a>
<a id="agroup__bt__aics_html_gade387c52d201ce10b39ef52157dae83d"></a>
<a id="agroup__bt__aics_html_gaecb9365a5e390111311d1b415a2cee79"></a>
<a id="agroup__bt__aics_html_gaf0b659698aa6a6a79143d4f591f67e09"></a>
<a id="agroup__bt__aics_html_gaf57896e2096a5e96ec46a56cdf216159"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_accbd6432732c88ad6adc5365800433b6"></a>
<a id="astructbt__aics__cb_html"></a>
<a id="astructbt__aics__cb_html_a1b54464a8c6df54993914da97da2f93d"></a>
<a id="astructbt__aics__cb_html_a1f13bdcfbfac65800f9e66dad48c3b78"></a>
<a id="astructbt__aics__cb_html_a41b6cac6ccc0195921d2e5a127d9091d"></a>
<a id="astructbt__aics__cb_html_a41bc7a97e28c53772573d99a38e8ac55"></a>
<a id="astructbt__aics__cb_html_a6b2f2a43d0a91abcecfe8372b6a1be4b"></a>
<a id="astructbt__aics__cb_html_a70d099bec6407e5c92f6a4e8d6c44929"></a>
<a id="astructbt__aics__cb_html_a80c8abd842706d2588e6a075cba61ba8"></a>
<a id="astructbt__aics__cb_html_aac9dccf825f5aa423212af4af3d4ca38"></a>
<a id="astructbt__aics__cb_html_ac89882943c293e533bec55dd285d7aa0"></a>
<a id="astructbt__aics__cb_html_ad37ae465600fa2e3c1868f0da07fd31a"></a>
<a id="astructbt__aics__cb_html_ae946f4b434b485774a3c8ddca5d86898"></a>
<a id="astructbt__aics__discover__param_html"></a>
<a id="astructbt__aics__discover__param_html_ab2931e7c4a627e717d943b2907b264cb"></a>
<a id="astructbt__aics__discover__param_html_ab867f7d2ae219df0c479cce72d68842f"></a>
<a id="astructbt__aics__register__param_html"></a>
<a id="astructbt__aics__register__param_html_a3658ed1900a44eef84b5602e567fe085"></a>
<a id="astructbt__aics__register__param_html_a46437f4540d226ce3fbc470448f36e1f"></a>
<a id="astructbt__aics__register__param_html_a4b2eae9a9716629e9c56ee3e6dc05e44"></a>
<a id="astructbt__aics__register__param_html_a6c961cde10dbfbaaa26bbc2b5c867001"></a>
<a id="astructbt__aics__register__param_html_a966e9e99544392cdfac264ee6effcc7c"></a>
<a id="astructbt__aics__register__param_html_aa139122e2710d9ec28ec015692545dda"></a>
<a id="astructbt__aics__register__param_html_aac91095a831fe540ee356eb9b9d402d8"></a>
<a id="astructbt__aics__register__param_html_ac95e17bc53539deeab5d161ca1b08194"></a>
<a id="astructbt__aics__register__param_html_acc408a0318b94cdc952ef7d6682e5705"></a>
<a id="astructbt__aics__register__param_html_ad6afebea920fa4c168498ca11778ea7d"></a>
<a id="astructbt__aics__register__param_html_af99d31215008eb201c488a5b1107e009"></a>
<a id="astructbt__aics_html"></a>
<a id="astructbt__conn_html"></a>

```c


/*
 * Copyright (c) 2020-2024 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_AICS_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_AICS_H_

#include <stdint.h>
#include <stdbool.h>

#include <zephyr/autoconf.h>
#include <zephyr/bluetooth/bluetooth.h>

#ifdef __cplusplus
extern "C" {
#endif

#define BT_AICS_STATE_UNMUTED                      0x00U
#define BT_AICS_STATE_MUTED                        0x01U
#define BT_AICS_STATE_MUTE_DISABLED                0x02U

#define BT_AICS_MODE_MANUAL_ONLY                   0x00U
#define BT_AICS_MODE_AUTO_ONLY                     0x01U
#define BT_AICS_MODE_MANUAL                        0x02U
#define BT_AICS_MODE_AUTO                          0x03U

static inline const char *bt_aics_mode_to_str(uint8_t mode)
{
        switch (mode) {
        case BT_AICS_MODE_MANUAL_ONLY:
                return "Manual only";
        case BT_AICS_MODE_AUTO_ONLY:
                return "Auto only";
        case BT_AICS_MODE_MANUAL:
                return "Manual";
        case BT_AICS_MODE_AUTO:
                return "Auto";
        default:
                return "Unknown";
        }
}

#define BT_AICS_INPUT_TYPE_UNSPECIFIED             0x00U
#define BT_AICS_INPUT_TYPE_BLUETOOTH               0x01U
#define BT_AICS_INPUT_TYPE_MICROPHONE              0x02U
#define BT_AICS_INPUT_TYPE_ANALOG                  0x03U
#define BT_AICS_INPUT_TYPE_DIGITAL                 0x04U
#define BT_AICS_INPUT_TYPE_RADIO                   0x05U
#define BT_AICS_INPUT_TYPE_STREAMING               0x06U
#define BT_AICS_INPUT_TYPE_AMBIENT                 0x07U

#define BT_AICS_ERR_INVALID_COUNTER                0x80U
#define BT_AICS_ERR_OP_NOT_SUPPORTED               0x81U
#define BT_AICS_ERR_MUTE_DISABLED                  0x82U
#define BT_AICS_ERR_OUT_OF_RANGE                   0x83U
#define BT_AICS_ERR_GAIN_MODE_NOT_ALLOWED          0x84U

struct bt_aics;

struct bt_aics_register_param {
        int8_t gain;

        uint8_t mute;

        uint8_t gain_mode;

        uint8_t units;

        int8_t min_gain;

        int8_t max_gain;

        uint8_t type;

        bool status;

        bool desc_writable;

        char *description;

        struct bt_aics_cb *cb;
};

struct bt_aics_discover_param {
        uint16_t start_handle;
        uint16_t end_handle;
};

struct bt_aics *bt_aics_free_instance_get(void);

void *bt_aics_svc_decl_get(struct bt_aics *aics);

int bt_aics_client_conn_get(const struct bt_aics *aics, struct bt_conn **conn);

int bt_aics_register(struct bt_aics *aics, struct bt_aics_register_param *param);

typedef void (*bt_aics_write_cb)(struct bt_aics *inst, int err);

typedef void (*bt_aics_state_cb)(struct bt_aics *inst, int err, int8_t gain,
                                 uint8_t mute, uint8_t mode);

typedef void (*bt_aics_gain_setting_cb)(struct bt_aics *inst, int err,
                                        uint8_t units, int8_t minimum,
                                        int8_t maximum);

typedef void (*bt_aics_type_cb)(struct bt_aics *inst, int err, uint8_t type);

typedef void (*bt_aics_status_cb)(struct bt_aics *inst, int err, bool active);

typedef void (*bt_aics_description_cb)(struct bt_aics *inst, int err,
                                       char *description);

typedef void (*bt_aics_discover_cb)(struct bt_aics *inst, int err);

struct bt_aics_cb {
        bt_aics_state_cb                 state;
        bt_aics_gain_setting_cb          gain_setting;
        bt_aics_type_cb                  type;
        bt_aics_status_cb                status;
        bt_aics_description_cb           description;

#if defined(CONFIG_BT_AICS_CLIENT) || defined(__DOXYGEN__)
        bt_aics_discover_cb              discover;
        bt_aics_write_cb                 set_gain;
        bt_aics_write_cb                 unmute;
        bt_aics_write_cb                 mute;
        bt_aics_write_cb                 set_manual_mode;
        bt_aics_write_cb                 set_auto_mode;
#endif /* CONFIG_BT_AICS_CLIENT */
};


int bt_aics_discover(struct bt_conn *conn, struct bt_aics *inst,
                     const struct bt_aics_discover_param *param);

int bt_aics_deactivate(struct bt_aics *inst);

int bt_aics_activate(struct bt_aics *inst);

int bt_aics_state_get(struct bt_aics *inst);

int bt_aics_gain_setting_get(struct bt_aics *inst);

int bt_aics_type_get(struct bt_aics *inst);

int bt_aics_status_get(struct bt_aics *inst);

int bt_aics_disable_mute(struct bt_aics *inst);

int bt_aics_unmute(struct bt_aics *inst);

int bt_aics_mute(struct bt_aics *inst);

int bt_aics_gain_set_manual_only(struct bt_aics *inst);

int bt_aics_gain_set_auto_only(struct bt_aics *inst);

int bt_aics_manual_gain_set(struct bt_aics *inst);

int bt_aics_automatic_gain_set(struct bt_aics *inst);

int bt_aics_gain_set(struct bt_aics *inst, int8_t gain);

int bt_aics_description_get(struct bt_aics *inst);

int bt_aics_description_set(struct bt_aics *inst, const char *description);

struct bt_aics *bt_aics_client_free_instance_get(void);

int bt_aics_client_free_instance(struct bt_aics *inst);

void bt_aics_client_cb_register(struct bt_aics *inst, struct bt_aics_cb *cb);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_AICS_H_ */
```

## 18.2\_可见注释译文（Comments）

### 注释 1：原第 6 行

版权（Copyright）：© 2020-2024 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 378 行

条件编译配置（Configuration）标记：`CONFIG_BT_AICS_CLIENT`。

### 注释 3：原第 592 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_AUDIO_AICS_H_`。

## 18.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/aics_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [zephyr/bluetooth/bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h.html)
- [bt_aics_mode_to_str](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga4d511e81dd0f0a72fd502bc05dd85e91)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [BT_AICS_MODE_MANUAL_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#gaecb9365a5e390111311d1b415a2cee79)
- [BT_AICS_MODE_AUTO_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga6b536bdcab602ccaccfafe3b37258890)
- [BT_AICS_MODE_MANUAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga7cf0508dd7407ec3bb92dec71cc00816)
- [BT_AICS_MODE_AUTO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga0ac3a583dd7ca58a0d356d9f60797517)
- [bt_aics](../bluetooth_le_audio_model_reference/P001_bt_aics_结构体.md)
- [bt_aics_register_param](../bluetooth_le_audio_model_reference/P004_bt_aics_register_param_结构体.md)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [gain](../bluetooth_le_audio_model_reference/P004_bt_aics_register_param_结构体.md#a966e9e99544392cdfac264ee6effcc7c)
- [mute](../bluetooth_le_audio_model_reference/P004_bt_aics_register_param_结构体.md#ac95e17bc53539deeab5d161ca1b08194)
- [gain_mode](../bluetooth_le_audio_model_reference/P004_bt_aics_register_param_结构体.md#a3658ed1900a44eef84b5602e567fe085)
- [units](../bluetooth_le_audio_model_reference/P004_bt_aics_register_param_结构体.md#a4b2eae9a9716629e9c56ee3e6dc05e44)
- [min_gain](../bluetooth_le_audio_model_reference/P004_bt_aics_register_param_结构体.md#aac91095a831fe540ee356eb9b9d402d8)
- [max_gain](../bluetooth_le_audio_model_reference/P004_bt_aics_register_param_结构体.md#aa139122e2710d9ec28ec015692545dda)
- [type](../bluetooth_le_audio_model_reference/P004_bt_aics_register_param_结构体.md#ad6afebea920fa4c168498ca11778ea7d)
- [status](../bluetooth_le_audio_model_reference/P004_bt_aics_register_param_结构体.md#a46437f4540d226ce3fbc470448f36e1f)
- [desc_writable](../bluetooth_le_audio_model_reference/P004_bt_aics_register_param_结构体.md#acc408a0318b94cdc952ef7d6682e5705)
- [description](../bluetooth_le_audio_model_reference/P004_bt_aics_register_param_结构体.md#af99d31215008eb201c488a5b1107e009)
- [bt_aics_cb](../bluetooth_le_audio_model_reference/P002_bt_aics_cb_结构体.md)
- [cb](../bluetooth_le_audio_model_reference/P004_bt_aics_register_param_结构体.md#a6c961cde10dbfbaaa26bbc2b5c867001)
- [bt_aics_discover_param](../bluetooth_le_audio_model_reference/P003_bt_aics_discover_param_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [start_handle](../bluetooth_le_audio_model_reference/P003_bt_aics_discover_param_结构体.md#ab867f7d2ae219df0c479cce72d68842f)
- [end_handle](../bluetooth_le_audio_model_reference/P003_bt_aics_discover_param_结构体.md#ab2931e7c4a627e717d943b2907b264cb)
- [bt_aics_free_instance_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#gab10ad3599f5b602cdf5504bc92508109)
- [bt_aics_svc_decl_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga8b415343e7ecf399ecfd0dcaa49bd1ee)
- [bt_aics_client_conn_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga0e088e26cf73f1f3b918660d4acdebb9)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_aics_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga008ef5cebfcb9b4a3084f411fa81238e)
- [bt_aics_write_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga36991fe1dee5168db618518d094d80ef)
- [bt_aics_state_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga2e851f49f9c7e71a18376468a13fdf4f)
- [bt_aics_gain_setting_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga11da08c010f4aa849c2e3725dc5cbaeb)
- [bt_aics_type_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga6e76b9f2de4cdbcd7539c76f6a347fa5)
- [bt_aics_status_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga044d92a4273c6537a9cdf20922352ed6)
- [bt_aics_description_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga98b142ea7a66de5577c44aa90d507930)
- [bt_aics_discover_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga9fda39f8410308e05eb928eeb7267e83)
- [state](../bluetooth_le_audio_model_reference/P002_bt_aics_cb_结构体.md#a70d099bec6407e5c92f6a4e8d6c44929)
- [gain_setting](../bluetooth_le_audio_model_reference/P002_bt_aics_cb_结构体.md#a6b2f2a43d0a91abcecfe8372b6a1be4b)
- [type](../bluetooth_le_audio_model_reference/P002_bt_aics_cb_结构体.md#a41bc7a97e28c53772573d99a38e8ac55)
- [status](../bluetooth_le_audio_model_reference/P002_bt_aics_cb_结构体.md#ac89882943c293e533bec55dd285d7aa0)
- [description](../bluetooth_le_audio_model_reference/P002_bt_aics_cb_结构体.md#ad37ae465600fa2e3c1868f0da07fd31a)
- [discover](../bluetooth_le_audio_model_reference/P002_bt_aics_cb_结构体.md#ae946f4b434b485774a3c8ddca5d86898)
- [set_gain](../bluetooth_le_audio_model_reference/P002_bt_aics_cb_结构体.md#a1f13bdcfbfac65800f9e66dad48c3b78)
- [unmute](../bluetooth_le_audio_model_reference/P002_bt_aics_cb_结构体.md#a80c8abd842706d2588e6a075cba61ba8)
- [mute](../bluetooth_le_audio_model_reference/P002_bt_aics_cb_结构体.md#a41b6cac6ccc0195921d2e5a127d9091d)
- [set_manual_mode](../bluetooth_le_audio_model_reference/P002_bt_aics_cb_结构体.md#a1b54464a8c6df54993914da97da2f93d)
- [set_auto_mode](../bluetooth_le_audio_model_reference/P002_bt_aics_cb_结构体.md#aac9dccf825f5aa423212af4af3d4ca38)
- [bt_aics_discover](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#gad16d296462af2f61a893bda8d25cc9de)
- [bt_aics_deactivate](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga4be4c4e3c74aa55fbf599157aa1c2098)
- [bt_aics_activate](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#gac46268949fa7cbbb827d149a3a904daa)
- [bt_aics_state_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga23bbc1393d21fe38f501813935b25b3d)
- [bt_aics_gain_setting_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga38d7131397d7762d3bd53e152a6c6130)
- [bt_aics_type_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#gaf57896e2096a5e96ec46a56cdf216159)
- [bt_aics_status_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#gade387c52d201ce10b39ef52157dae83d)
- [bt_aics_disable_mute](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga5a1ad98afe45da9ffbb7247671385d40)
- [bt_aics_unmute](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga43396d2d4b3bd9cdd0c82275fafeadfc)
- [bt_aics_mute](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga5345254eaf099560e609d97044b39a97)
- [bt_aics_gain_set_manual_only](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga0460e82d4277a2c4b14964799ad5f2b0)
- [bt_aics_gain_set_auto_only](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga22869d8a62eb59bc4aad25946da8f9cf)
- [bt_aics_manual_gain_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga7ddb93125f6275fc7c99fbf448e24f0c)
- [bt_aics_automatic_gain_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga759712886cd3c4c025ea360dcb663c59)
- [bt_aics_gain_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga20f3a178788ec6aef593034159793b94)
- [bt_aics_description_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#gaf0b659698aa6a6a79143d4f591f67e09)
- [bt_aics_description_set](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga7de5ffd2eb61ca562b9773b37470ebd9)
- [bt_aics_client_free_instance_get](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga913838aa0d5bff239c2faef4d8a8b36b)
- [bt_aics_client_free_instance](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#gab660d2d4603de3837a3b93ce11e4d0fd)
- [bt_aics_client_cb_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#gabd6bdcdad0dd5a4c509f9e7cabb3e601)
- [bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h.html)
- [bt_aics_cb::set_manual_mode](../bluetooth_le_audio_model_reference/P002_bt_aics_cb_结构体.md#a1b54464a8c6df54993914da97da2f93d)
- [bt_aics_cb::set_gain](../bluetooth_le_audio_model_reference/P002_bt_aics_cb_结构体.md#a1f13bdcfbfac65800f9e66dad48c3b78)
- [bt_aics_cb::mute](../bluetooth_le_audio_model_reference/P002_bt_aics_cb_结构体.md#a41b6cac6ccc0195921d2e5a127d9091d)
- [bt_aics_cb::type](../bluetooth_le_audio_model_reference/P002_bt_aics_cb_结构体.md#a41bc7a97e28c53772573d99a38e8ac55)
- [bt_aics_cb::gain_setting](../bluetooth_le_audio_model_reference/P002_bt_aics_cb_结构体.md#a6b2f2a43d0a91abcecfe8372b6a1be4b)
- [bt_aics_cb::state](../bluetooth_le_audio_model_reference/P002_bt_aics_cb_结构体.md#a70d099bec6407e5c92f6a4e8d6c44929)
- [bt_aics_cb::unmute](../bluetooth_le_audio_model_reference/P002_bt_aics_cb_结构体.md#a80c8abd842706d2588e6a075cba61ba8)
- [bt_aics_cb::set_auto_mode](../bluetooth_le_audio_model_reference/P002_bt_aics_cb_结构体.md#aac9dccf825f5aa423212af4af3d4ca38)
- [bt_aics_cb::status](../bluetooth_le_audio_model_reference/P002_bt_aics_cb_结构体.md#ac89882943c293e533bec55dd285d7aa0)
- [bt_aics_cb::description](../bluetooth_le_audio_model_reference/P002_bt_aics_cb_结构体.md#ad37ae465600fa2e3c1868f0da07fd31a)
- [bt_aics_cb::discover](../bluetooth_le_audio_model_reference/P002_bt_aics_cb_结构体.md#ae946f4b434b485774a3c8ddca5d86898)
- [bt_aics_discover_param::end_handle](../bluetooth_le_audio_model_reference/P003_bt_aics_discover_param_结构体.md#ab2931e7c4a627e717d943b2907b264cb)
- [bt_aics_discover_param::start_handle](../bluetooth_le_audio_model_reference/P003_bt_aics_discover_param_结构体.md#ab867f7d2ae219df0c479cce72d68842f)
- [bt_aics_register_param::gain_mode](../bluetooth_le_audio_model_reference/P004_bt_aics_register_param_结构体.md#a3658ed1900a44eef84b5602e567fe085)
- [bt_aics_register_param::status](../bluetooth_le_audio_model_reference/P004_bt_aics_register_param_结构体.md#a46437f4540d226ce3fbc470448f36e1f)
- [bt_aics_register_param::units](../bluetooth_le_audio_model_reference/P004_bt_aics_register_param_结构体.md#a4b2eae9a9716629e9c56ee3e6dc05e44)
- [bt_aics_register_param::cb](../bluetooth_le_audio_model_reference/P004_bt_aics_register_param_结构体.md#a6c961cde10dbfbaaa26bbc2b5c867001)
- [bt_aics_register_param::gain](../bluetooth_le_audio_model_reference/P004_bt_aics_register_param_结构体.md#a966e9e99544392cdfac264ee6effcc7c)
- [bt_aics_register_param::max_gain](../bluetooth_le_audio_model_reference/P004_bt_aics_register_param_结构体.md#aa139122e2710d9ec28ec015692545dda)
- [bt_aics_register_param::min_gain](../bluetooth_le_audio_model_reference/P004_bt_aics_register_param_结构体.md#aac91095a831fe540ee356eb9b9d402d8)
- [bt_aics_register_param::mute](../bluetooth_le_audio_model_reference/P004_bt_aics_register_param_结构体.md#ac95e17bc53539deeab5d161ca1b08194)
- [bt_aics_register_param::desc_writable](../bluetooth_le_audio_model_reference/P004_bt_aics_register_param_结构体.md#acc408a0318b94cdc952ef7d6682e5705)
- [bt_aics_register_param::type](../bluetooth_le_audio_model_reference/P004_bt_aics_register_param_结构体.md#ad6afebea920fa4c168498ca11778ea7d)
- [bt_aics_register_param::description](../bluetooth_le_audio_model_reference/P004_bt_aics_register_param_结构体.md#af99d31215008eb201c488a5b1107e009)

---

[上一章](P017_aesc-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P019_alif-balletto-b1-pinctrl.h_源码浏览.md)
