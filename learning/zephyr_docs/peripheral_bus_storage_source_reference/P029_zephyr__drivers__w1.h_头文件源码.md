---
id: learning.zephyr-docs.peripheral-bus-storage-source-reference.page-29
title: zephyr__drivers__w1.h_头文件源码
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/w1_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第29章\_zephyr__drivers__w1.h_头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/w1_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应头文件参考](../peripheral_bus_storage_header_reference/P029_zephyr__drivers__w1.h_头文件参考.md)。

## 29.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
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
<a id="l00035"></a>
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
<a id="l00052"></a>
<a id="foldopen00056"></a>
<a id="l00056"></a>
<a id="l00060"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00077"></a>
<a id="foldopen00085"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="foldopen00097"></a>
<a id="l00097"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="foldopen00168"></a>
<a id="l00168"></a>
<a id="l00170"></a>
<a id="l00172"></a>
<a id="l00174"></a>
<a id="l00176"></a>
<a id="l00178"></a>
<a id="l00185"></a>
<a id="l00192"></a>
<a id="l00194"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00204"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00224"></a>
<a id="foldopen00236"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="foldopen00250"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00261"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="l00295"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00310"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00324"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="l00327"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="l00330"></a>
<a id="l00339"></a>
<a id="l00340"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="l00343"></a>
<a id="l00344"></a>
<a id="l00345"></a>
<a id="l00355"></a>
<a id="l00356"></a>
<a id="l00366"></a>
<a id="l00367"></a>
<a id="l00368"></a>
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
<a id="l00400"></a>
<a id="l00401"></a>
<a id="l00402"></a>
<a id="l00403"></a>
<a id="l00404"></a>
<a id="l00405"></a>
<a id="l00406"></a>
<a id="l00407"></a>
<a id="l00408"></a>
<a id="l00412"></a>
<a id="l00419"></a>
<a id="l00424"></a>
<a id="l00429"></a>
<a id="l00430"></a>
<a id="l00435"></a>
<a id="l00436"></a>
<a id="l00441"></a>
<a id="l00442"></a>
<a id="l00449"></a>
<a id="l00450"></a>
<a id="l00455"></a>
<a id="l00456"></a>
<a id="l00461"></a>
<a id="l00462"></a>
<a id="l00467"></a>
<a id="l00468"></a>
<a id="l00473"></a>
<a id="l00474"></a>
<a id="l00476"></a>
<a id="l00481"></a>
<a id="l00483"></a>
<a id="l00485"></a>
<a id="l00487"></a>
<a id="l00489"></a>
<a id="l00490"></a>
<a id="l00492"></a>
<a id="l00494"></a>
<a id="l00495"></a>
<a id="foldopen00497"></a>
<a id="l00497"></a>
<a id="l00498"></a>
<a id="l00499"></a>
<a id="l00500"></a>
<a id="l00501"></a>
<a id="foldopen00505"></a>
<a id="l00505"></a>
<a id="l00512"></a>
<a id="l00514"></a>
<a id="l00516"></a>
<a id="l00517"></a>
<a id="l00518"></a>
<a id="foldopen00525"></a>
<a id="l00525"></a>
<a id="l00527"></a>
<a id="l00529"></a>
<a id="l00531"></a>
<a id="l00533"></a>
<a id="l00534"></a>
<a id="l00542"></a>
<a id="l00543"></a>
<a id="l00559"></a>
<a id="l00560"></a>
<a id="l00580"></a>
<a id="l00581"></a>
<a id="l00593"></a>
<a id="l00594"></a>
<a id="l00609"></a>
<a id="l00610"></a>
<a id="l00621"></a>
<a id="l00622"></a>
<a id="l00639"></a>
<a id="l00640"></a>
<a id="l00641"></a>
<a id="l00642"></a>
<a id="l00666"></a>
<a id="l00667"></a>
<a id="l00668"></a>
<a id="l00669"></a>
<a id="foldopen00684"></a>
<a id="l00684"></a>
<a id="l00685"></a>
<a id="l00686"></a>
<a id="l00687"></a>
<a id="l00688"></a>
<a id="l00689"></a>
<a id="l00690"></a>
<a id="foldopen00705"></a>
<a id="l00705"></a>
<a id="l00706"></a>
<a id="l00707"></a>
<a id="l00708"></a>
<a id="l00709"></a>
<a id="l00710"></a>
<a id="l00711"></a>
<a id="foldopen00719"></a>
<a id="l00719"></a>
<a id="l00720"></a>
<a id="l00721"></a>
<a id="l00722"></a>
<a id="l00723"></a>
<a id="foldopen00730"></a>
<a id="l00730"></a>
<a id="l00731"></a>
<a id="l00732"></a>
<a id="l00733"></a>
<a id="l00734"></a>
<a id="foldopen00747"></a>
<a id="l00747"></a>
<a id="l00748"></a>
<a id="l00749"></a>
<a id="l00750"></a>
<a id="l00751"></a>
<a id="foldopen00767"></a>
<a id="l00767"></a>
<a id="l00768"></a>
<a id="l00769"></a>
<a id="l00770"></a>
<a id="l00771"></a>
<a id="l00772"></a>
<a id="l00776"></a>
<a id="l00777"></a>
<a id="l00778"></a>
<a id="l00779"></a>
<a id="l00780"></a>
<a id="l00784"></a>
<a id="l00785"></a>
<a id="l00786"></a>
<a id="adevice_8h_html"></a>
<a id="adevice_8h_html_a9907e8ee5e7be8c3b5d52b13bd33970a"></a>
<a id="agroup__clock__apis_html_ga0bb4b83f0222193b21a8910311bab0ca"></a>
<a id="agroup__crc_html_gaa614e73ee7484ca0424fa7d14a54bbb6"></a>
<a id="agroup__crc_html_gaccbcb5b80cf8deaac252474ecc6d9914"></a>
<a id="agroup__mutex__apis_html_ga360f4c0e7258b0d7030cdb1f452b2c31"></a>
<a id="agroup__mutex__apis_html_ga850549358645249c285669baa49c33b0"></a>
<a id="agroup__w1__data__link_html_ga0f2b37163f3d7c9816371942765509b4"></a>
<a id="agroup__w1__data__link_html_ga2967c99ec93b7c31beb9cf2a327a23f4"></a>
<a id="agroup__w1__data__link_html_ga3671d8bbf9d044c60d7e96e4190ba2fa"></a>
<a id="agroup__w1__data__link_html_ga65892855c763dccc27b508d870c1d144"></a>
<a id="agroup__w1__data__link_html_ga868980684bb98149af5b59e3fa8a83b6"></a>
<a id="agroup__w1__data__link_html_ga978a8f14fb8cb3a569f8b731b20cc840"></a>
<a id="agroup__w1__data__link_html_gab30a58c42c06088da9e0845de7d089ce"></a>
<a id="agroup__w1__data__link_html_gab4eccd585c6f14330807055ccc151fd6"></a>
<a id="agroup__w1__data__link_html_gae989e0deebe5666edc9ff8a3839cf216"></a>
<a id="agroup__w1__interface__backend_html_ga126e501ef9a74cbc3c375ca64025cdbc"></a>
<a id="agroup__w1__interface__backend_html_ga18924f833820d5f70d73ab33de6615dd"></a>
<a id="agroup__w1__interface__backend_html_ga5d3ee84858e35cdac923a6238a22e9a2"></a>
<a id="agroup__w1__interface__backend_html_ga861af0744a5f102558294422de50f6ae"></a>
<a id="agroup__w1__interface__backend_html_ga87232322cd487772d377aa0a8e9e5bfc"></a>
<a id="agroup__w1__interface__backend_html_gaa64e8b894df8a3a44f3b91ea647cc0c1"></a>
<a id="agroup__w1__interface__backend_html_gab831da9314fce3e6ec10526ca5224515"></a>
<a id="agroup__w1__interface__backend_html_gabb495014dd7b9583009b34d9eba02ddc"></a>
<a id="agroup__w1__interface__backend_html_gae2673a21841ad196af69e5b4e6769ea8"></a>
<a id="agroup__w1__interface__backend_html_gafbbba20705697154d29a91ac94cc3747"></a>
<a id="agroup__w1__interface_html_ga382989ef707709b5d26c40a394833612"></a>
<a id="agroup__w1__interface_html_ga7230fad2428ab62fa963b50e67388c19"></a>
<a id="agroup__w1__interface_html_gab18b0f60a126d38c982730d3ad9756c1"></a>
<a id="agroup__w1__interface_html_gga382989ef707709b5d26c40a394833612a788fee2803793832c58951d623d823d5"></a>
<a id="agroup__w1__interface_html_gga382989ef707709b5d26c40a394833612a814e27d05a04e027c52cb206aaf69b22"></a>
<a id="agroup__w1__interface_html_gga382989ef707709b5d26c40a394833612ae3293dfeaa3f1976e8cf57e694d5f811"></a>
<a id="agroup__w1__network_html_ga024af0ee5018d7078808cc0a544cfd26"></a>
<a id="agroup__w1__network_html_ga0f510bd3720e54b4eeb4e368934db7f0"></a>
<a id="agroup__w1__network_html_ga178a88d0c585d5df0405aadde3ea9178"></a>
<a id="agroup__w1__network_html_ga19533f445029a69aac7d4ca5a7aeedcd"></a>
<a id="agroup__w1__network_html_ga1cf8c016ac66c3970f72fa1f409fa680"></a>
<a id="agroup__w1__network_html_ga2f5540f2a86fd55edcd7a8ffecbfd786"></a>
<a id="agroup__w1__network_html_ga350a384a6040d1fbb86bfb804013ade3"></a>
<a id="agroup__w1__network_html_ga53f34d64504498dbb194bc2119727908"></a>
<a id="agroup__w1__network_html_ga5635f79a54a2e5b96c8b7ca9a8ab8366"></a>
<a id="agroup__w1__network_html_ga57f17871edab0b771f2f664bf9bafb79"></a>
<a id="agroup__w1__network_html_ga67c815bb99b75c862a483d4f8556b24a"></a>
<a id="agroup__w1__network_html_ga6e4dba051a6b29c974e499db17315034"></a>
<a id="agroup__w1__network_html_ga909502b9b18c15a9ab0da8d3605e8c37"></a>
<a id="agroup__w1__network_html_ga93abefbd0e7067db474e6480301a0c4c"></a>
<a id="agroup__w1__network_html_gaa0acc88fe02535a3d512b866b6d34b8a"></a>
<a id="agroup__w1__network_html_gaa4ad8d9a3791fbca6c99d49b9793a002"></a>
<a id="agroup__w1__network_html_gab94362fbf4eec5f115f93fc8976cff0d"></a>
<a id="agroup__w1__network_html_gaba2be4e87ff472e90b705dbd73b913de"></a>
<a id="agroup__w1__network_html_gabe56ffbe20c2ba7e0a5c87c8e36c45e5"></a>
<a id="agroup__w1__network_html_gafc7a257428c69bb4549c6cd05a928957"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_a27573cbd10ee145f8bb1396242b27a3e"></a>
<a id="astructdevice_html_aca2d801eb15996cf1c74dc65cfa651fc"></a>
<a id="astructk__mutex_html"></a>
<a id="astructw1__driver__api_html"></a>
<a id="astructw1__driver__api_html_a145e07fc821cf21795db761f6c82d650"></a>
<a id="astructw1__driver__api_html_a1ee0dae9846d2e7ba9a016d3333b040e"></a>
<a id="astructw1__driver__api_html_a2c3312afc1929fafed6db5607e4f7d2c"></a>
<a id="astructw1__driver__api_html_a34ea6f69f0cc3502a5639f7a5a3c3c1f"></a>
<a id="astructw1__driver__api_html_a84f92f1c855550e54a4c5d53e72af5c7"></a>
<a id="astructw1__driver__api_html_ac89908044403cd1d8768425617bd1b86"></a>
<a id="astructw1__driver__api_html_ae7d6cef0458e281c1b653a4e6ecbe3f1"></a>
<a id="astructw1__driver__api_html_ae930e72652123e0f616ed59ebf179f0c"></a>
<a id="astructw1__driver__api_html_aec4d570356600e1c769626d3cb9e75f2"></a>
<a id="astructw1__master__config_html"></a>
<a id="astructw1__master__config_html_a5cf7b0808d939ad7a6fec4540c36f4c4"></a>
<a id="astructw1__master__data_html"></a>
<a id="astructw1__master__data_html_af9cc46f803aff0d5e0d8ca345aaf8b9e"></a>
<a id="astructw1__rom_html"></a>
<a id="astructw1__rom_html_a134ee6d6e5e5eb711caf59449d11732e"></a>
<a id="astructw1__rom_html_a73d85d7ce0ef671027c910b9b7a54165"></a>
<a id="astructw1__rom_html_adc7f4f9fca172392b11864a17424a14c"></a>
<a id="astructw1__slave__config_html"></a>
<a id="astructw1__slave__config_html_a9f42fd1257483f308115ae02e6ef8596"></a>
<a id="astructw1__slave__config_html_ab8a2d4522505416863fed561df22d058"></a>
<a id="asys_2byteorder_8h_html"></a>
<a id="asys_2byteorder_8h_html_a3e0d2e4e85249497011f5f9ea0d2987c"></a>
<a id="asys_2byteorder_8h_html_ad8e00ff5c0b9e394291936d1a570c215"></a>
<a id="asys_2crc_8h_html"></a>

```c
/*
 * Copyright (c) 2018 Roman Tataurov <diytronic@yandex.ru>
 * Copyright (c) 2022 Thomas Stranger
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DRIVERS_W1_H_
#define ZEPHYR_INCLUDE_DRIVERS_W1_H_

#include <zephyr/types.h>
#include <zephyr/device.h>
#include <zephyr/kernel.h>
#include <zephyr/sys/crc.h>
#include <zephyr/sys/byteorder.h>

#ifdef __cplusplus
extern "C" {
#endif



/*
 * Count the number of slaves expected on the bus.
 * This can be used to decide if the bus has a multidrop topology or
 * only a single slave is present.
 * There is a comma after each ordinal (including the last)
 * Hence FOR_EACH adds "+1" once too often which has to be subtracted in the end.
 */
#define F1(x) 1
#define W1_SLAVE_COUNT(node_id) \
                (FOR_EACH(F1, (+), DT_SUPPORTS_DEP_ORDS(node_id)) - 1)
#define W1_INST_SLAVE_COUNT(inst)  \
                (W1_SLAVE_COUNT(DT_DRV_INST(inst)))


enum w1_settings_type {
        W1_SETTING_SPEED,
        W1_SETTING_STRONG_PULLUP,

        W1_SETINGS_TYPE_COUNT,
};


struct w1_master_config {
        uint16_t slave_count;
};

struct w1_master_data {
        struct k_mutex bus_lock;
};

typedef int (*w1_reset_bus_t)(const struct device *dev);

typedef int (*w1_read_bit_t)(const struct device *dev);

typedef int (*w1_write_bit_t)(const struct device *dev, bool bit);

typedef int (*w1_read_byte_t)(const struct device *dev);

typedef int (*w1_write_byte_t)(const struct device *dev, const uint8_t byte);

typedef int (*w1_read_block_t)(const struct device *dev, uint8_t *buffer,
                               size_t len);

typedef int (*w1_write_block_t)(const struct device *dev, const uint8_t *buffer,
                                size_t len);

typedef size_t (*w1_get_slave_count_t)(const struct device *dev);

typedef int (*w1_configure_t)(const struct device *dev,
                              enum w1_settings_type type, uint32_t value);

typedef int (*w1_change_bus_lock_t)(const struct device *dev, bool lock);

__subsystem struct w1_driver_api {
        w1_reset_bus_t reset_bus;
        w1_read_bit_t read_bit;
        w1_write_bit_t write_bit;
        w1_read_byte_t read_byte;
        w1_write_byte_t write_byte;
        w1_read_block_t read_block;
        w1_write_block_t write_block;
        w1_configure_t configure;
        w1_change_bus_lock_t change_bus_lock;
};


__syscall int w1_change_bus_lock(const struct device *dev, bool lock);

static inline int z_impl_w1_change_bus_lock(const struct device *dev, bool lock)
{
        struct w1_master_data *ctrl_data = (struct w1_master_data *)dev->data;
        const struct w1_driver_api *api = DEVICE_API_GET(w1, dev);

        if (api->change_bus_lock) {
                return api->change_bus_lock(dev, lock);
        }

        if (lock) {
                return k_mutex_lock(&ctrl_data->bus_lock, K_FOREVER);
        } else {
                return k_mutex_unlock(&ctrl_data->bus_lock);
        }
}

static inline int w1_lock_bus(const struct device *dev)
{
        return w1_change_bus_lock(dev, true);
}

static inline int w1_unlock_bus(const struct device *dev)
{
        return w1_change_bus_lock(dev, false);
}


__syscall int w1_reset_bus(const struct device *dev);

static inline int z_impl_w1_reset_bus(const struct device *dev)
{
        return DEVICE_API_GET(w1, dev)->reset_bus(dev);
}

__syscall int w1_read_bit(const struct device *dev);

static inline int z_impl_w1_read_bit(const struct device *dev)
{
        return DEVICE_API_GET(w1, dev)->read_bit(dev);
}

__syscall int w1_write_bit(const struct device *dev, const bool bit);

static inline int z_impl_w1_write_bit(const struct device *dev, bool bit)
{
        return DEVICE_API_GET(w1, dev)->write_bit(dev, bit);
}

__syscall int w1_read_byte(const struct device *dev);

static inline int z_impl_w1_read_byte(const struct device *dev)
{
        return DEVICE_API_GET(w1, dev)->read_byte(dev);
}

__syscall int w1_write_byte(const struct device *dev, uint8_t byte);

static inline int z_impl_w1_write_byte(const struct device *dev, uint8_t byte)
{
        return DEVICE_API_GET(w1, dev)->write_byte(dev, byte);
}

__syscall int w1_read_block(const struct device *dev, uint8_t *buffer, size_t len);

__syscall int w1_write_block(const struct device *dev,
                             const uint8_t *buffer, size_t len);

__syscall size_t w1_get_slave_count(const struct device *dev);

static inline size_t z_impl_w1_get_slave_count(const struct device *dev)
{
        const struct w1_master_config *ctrl_cfg =
                (const struct w1_master_config *)dev->config;

        return ctrl_cfg->slave_count;
}

__syscall int w1_configure(const struct device *dev,
                           enum w1_settings_type type, uint32_t value);

static inline int z_impl_w1_configure(const struct device *dev,
                                      enum w1_settings_type type, uint32_t value)
{
        return DEVICE_API_GET(w1, dev)->configure(dev, type, value);
}




#define W1_CMD_SKIP_ROM                 0xCC

#define W1_CMD_MATCH_ROM                0x55

#define W1_CMD_RESUME                   0xA5

#define W1_CMD_READ_ROM                 0x33

#define W1_CMD_SEARCH_ROM               0xF0

#define W1_CMD_SEARCH_ALARM             0xEC

#define W1_CMD_OVERDRIVE_SKIP_ROM       0x3C

#define W1_CMD_OVERDRIVE_MATCH_ROM      0x69



#define W1_CRC8_SEED            0x00
#define W1_CRC8_POLYNOMIAL      0x8C
#define W1_CRC16_SEED           0x0000
#define W1_CRC16_POLYNOMIAL     0xa001


#define W1_SEARCH_ALL_FAMILIES          0x00

#define W1_ROM_INIT_ZERO                                        \
        {                                                       \
                .family = 0, .serial = { 0 }, .crc = 0,         \
        }

struct w1_rom {
        uint8_t family;
        uint8_t serial[6];
        uint8_t crc;
};

struct w1_slave_config {
        struct w1_rom rom;
        uint32_t overdrive : 1;
        uint32_t res : 31;
};

typedef void (*w1_search_callback_t)(struct w1_rom rom, void *user_data);

int w1_read_rom(const struct device *dev, struct w1_rom *rom);

int w1_match_rom(const struct device *dev, const struct w1_slave_config *config);

int w1_resume_command(const struct device *dev);

int w1_skip_rom(const struct device *dev, const struct w1_slave_config *config);

int w1_reset_select(const struct device *dev, const struct w1_slave_config *config);

int w1_write_read(const struct device *dev, const struct w1_slave_config *config,
                  const uint8_t *write_buf, size_t write_len,
                  uint8_t *read_buf, size_t read_len);

__syscall int w1_search_bus(const struct device *dev, uint8_t command,
                            uint8_t family, w1_search_callback_t callback,
                            void *user_data);

static inline int w1_search_rom(const struct device *dev,
                                w1_search_callback_t callback, void *user_data)
{
        return w1_search_bus(dev, W1_CMD_SEARCH_ROM, W1_SEARCH_ALL_FAMILIES,
                             callback, user_data);
}

static inline int w1_search_alarm(const struct device *dev,
                                  w1_search_callback_t callback, void *user_data)
{
        return w1_search_bus(dev, W1_CMD_SEARCH_ALARM, W1_SEARCH_ALL_FAMILIES,
                             callback, user_data);
}

static inline uint64_t w1_rom_to_uint64(const struct w1_rom *rom)
{
        return sys_get_be64((uint8_t *)rom);
}

static inline void w1_uint64_to_rom(const uint64_t rom64, struct w1_rom *rom)
{
        sys_put_be64(rom64, (uint8_t *)rom);
}

static inline uint8_t w1_crc8(const uint8_t *src, size_t len)
{
        return crc8(src, len, W1_CRC8_POLYNOMIAL, W1_CRC8_SEED, true);
}

static inline uint16_t w1_crc16(const uint16_t seed, const uint8_t *src,
                                const size_t len)
{
        return crc16_reflect(W1_CRC16_POLYNOMIAL, seed, src, len);
}


#ifdef __cplusplus
}
#endif

#include <zephyr/syscalls/w1.h>

#endif /* ZEPHYR_INCLUDE_DRIVERS_W1_H_ */
```

## 29.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2018 Roman Tataurov <diytronic@yandex.ru>。

版权（Copyright）：© 2022 Thomas Stranger。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 38 行

统计总线上预期的从设备数量。可据此判断总线采用多从设备拓扑（Multidrop topology），还是仅有一个从设备。每个序号后都带有逗号，包括最后一个，因此 `FOR_EACH` 会额外多加一次 `+1`，必须在最后减去。

### 注释 3：原第 786 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_W1_H_`。

## 29.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../peripheral_bus_storage_header_reference/P029_zephyr__drivers__w1.h_头文件参考.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/sys/crc.h](../data_utilities/P004_CRC系统头文件.md)
- [zephyr/sys/byteorder.h](../byteorder_reference/P001_系统字节序头文件参考.md)
- [w1_settings_type](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface.html#ga382989ef707709b5d26c40a394833612)
- [W1_SETTING_SPEED](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface.html#gga382989ef707709b5d26c40a394833612a788fee2803793832c58951d623d823d5)
- [W1_SETTING_STRONG_PULLUP](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface.html#gga382989ef707709b5d26c40a394833612ae3293dfeaa3f1976e8cf57e694d5f811)
- [W1_SETINGS_TYPE_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface.html#gga382989ef707709b5d26c40a394833612a814e27d05a04e027c52cb206aaf69b22)
- [w1_master_config](../peripheral_bus_storage_model_reference/P096_w1_master_config_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [slave_count](../peripheral_bus_storage_model_reference/P096_w1_master_config_结构体.md#a5cf7b0808d939ad7a6fec4540c36f4c4)
- [w1_master_data](../peripheral_bus_storage_model_reference/P097_w1_master_data_结构体.md)
- [k_mutex](../synchronization_reference/P007_内核互斥量结构.md)
- [bus_lock](../peripheral_bus_storage_model_reference/P097_w1_master_data_结构体.md#af9cc46f803aff0d5e0d8ca345aaf8b9e)
- [w1_reset_bus_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html#ga87232322cd487772d377aa0a8e9e5bfc)
- [device](../device_reference/P002_设备对象结构.md)
- [w1_read_bit_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html#gabb495014dd7b9583009b34d9eba02ddc)
- [w1_write_bit_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html#ga126e501ef9a74cbc3c375ca64025cdbc)
- [w1_read_byte_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html#ga861af0744a5f102558294422de50f6ae)
- [w1_write_byte_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html#ga18924f833820d5f70d73ab33de6615dd)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [w1_read_block_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html#gae2673a21841ad196af69e5b4e6769ea8)
- [w1_write_block_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html#gafbbba20705697154d29a91ac94cc3747)
- [w1_get_slave_count_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html#ga5d3ee84858e35cdac923a6238a22e9a2)
- [w1_configure_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html#gab831da9314fce3e6ec10526ca5224515)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [w1_change_bus_lock_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html#gaa64e8b894df8a3a44f3b91ea647cc0c1)
- [w1_driver_api](../peripheral_bus_storage_model_reference/P095_w1_driver_api_结构体.md)
- [reset_bus](../peripheral_bus_storage_model_reference/P095_w1_driver_api_结构体.md#a2c3312afc1929fafed6db5607e4f7d2c)
- [read_bit](../peripheral_bus_storage_model_reference/P095_w1_driver_api_结构体.md#ae7d6cef0458e281c1b653a4e6ecbe3f1)
- [write_bit](../peripheral_bus_storage_model_reference/P095_w1_driver_api_结构体.md#ac89908044403cd1d8768425617bd1b86)
- [read_byte](../peripheral_bus_storage_model_reference/P095_w1_driver_api_结构体.md#aec4d570356600e1c769626d3cb9e75f2)
- [write_byte](../peripheral_bus_storage_model_reference/P095_w1_driver_api_结构体.md#ae930e72652123e0f616ed59ebf179f0c)
- [read_block](../peripheral_bus_storage_model_reference/P095_w1_driver_api_结构体.md#a84f92f1c855550e54a4c5d53e72af5c7)
- [write_block](../peripheral_bus_storage_model_reference/P095_w1_driver_api_结构体.md#a145e07fc821cf21795db761f6c82d650)
- [configure](../peripheral_bus_storage_model_reference/P095_w1_driver_api_结构体.md#a1ee0dae9846d2e7ba9a016d3333b040e)
- [change_bus_lock](../peripheral_bus_storage_model_reference/P095_w1_driver_api_结构体.md#a34ea6f69f0cc3502a5639f7a5a3c3c1f)
- [data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [DEVICE_API_GET](../device_reference/P007_设备模型头文件参考.md#a9907e8ee5e7be8c3b5d52b13bd33970a)
- [k_mutex_lock](../synchronization_reference/P006_互斥量公共接口.md#ga850549358645249c285669baa49c33b0)
- [K_FOREVER](../timer_reference/P086_系统时钟公共接口.md#ga0bb4b83f0222193b21a8910311bab0ca)
- [k_mutex_unlock](../synchronization_reference/P006_互斥量公共接口.md#ga360f4c0e7258b0d7030cdb1f452b2c31)
- [w1_lock_bus](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface.html#gab18b0f60a126d38c982730d3ad9756c1)
- [w1_unlock_bus](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface.html#ga7230fad2428ab62fa963b50e67388c19)
- [w1_reset_bus](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__data__link.html#gab4eccd585c6f14330807055ccc151fd6)
- [w1_read_bit](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__data__link.html#ga0f2b37163f3d7c9816371942765509b4)
- [w1_write_bit](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__data__link.html#ga3671d8bbf9d044c60d7e96e4190ba2fa)
- [w1_read_byte](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__data__link.html#ga868980684bb98149af5b59e3fa8a83b6)
- [w1_write_byte](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__data__link.html#ga978a8f14fb8cb3a569f8b731b20cc840)
- [w1_read_block](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__data__link.html#ga2967c99ec93b7c31beb9cf2a327a23f4)
- [w1_write_block](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__data__link.html#gab30a58c42c06088da9e0845de7d089ce)
- [w1_get_slave_count](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__data__link.html#ga65892855c763dccc27b508d870c1d144)
- [config](../device_reference/P002_设备对象结构.md#aca2d801eb15996cf1c74dc65cfa651fc)
- [w1_configure](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__data__link.html#gae989e0deebe5666edc9ff8a3839cf216)
- [w1_rom](../peripheral_bus_storage_model_reference/P098_w1_rom_结构体.md)
- [family](../peripheral_bus_storage_model_reference/P098_w1_rom_结构体.md#adc7f4f9fca172392b11864a17424a14c)
- [serial](../peripheral_bus_storage_model_reference/P098_w1_rom_结构体.md#a134ee6d6e5e5eb711caf59449d11732e)
- [crc](../peripheral_bus_storage_model_reference/P098_w1_rom_结构体.md#a73d85d7ce0ef671027c910b9b7a54165)
- [w1_slave_config](../peripheral_bus_storage_model_reference/P099_w1_slave_config_结构体.md)
- [rom](../peripheral_bus_storage_model_reference/P099_w1_slave_config_结构体.md#a9f42fd1257483f308115ae02e6ef8596)
- [overdrive](../peripheral_bus_storage_model_reference/P099_w1_slave_config_结构体.md#ab8a2d4522505416863fed561df22d058)
- [w1_search_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga2f5540f2a86fd55edcd7a8ffecbfd786)
- [w1_read_rom](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga93abefbd0e7067db474e6480301a0c4c)
- [w1_match_rom](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga53f34d64504498dbb194bc2119727908)
- [w1_resume_command](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga67c815bb99b75c862a483d4f8556b24a)
- [w1_skip_rom](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#gaba2be4e87ff472e90b705dbd73b913de)
- [w1_reset_select](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#gaa0acc88fe02535a3d512b866b6d34b8a)
- [w1_write_read](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga1cf8c016ac66c3970f72fa1f409fa680)
- [w1_search_bus](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga19533f445029a69aac7d4ca5a7aeedcd)
- [w1_search_rom](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga024af0ee5018d7078808cc0a544cfd26)
- [W1_CMD_SEARCH_ROM](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga57f17871edab0b771f2f664bf9bafb79)
- [W1_SEARCH_ALL_FAMILIES](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga909502b9b18c15a9ab0da8d3605e8c37)
- [w1_search_alarm](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga0f510bd3720e54b4eeb4e368934db7f0)
- [W1_CMD_SEARCH_ALARM](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#gafc7a257428c69bb4549c6cd05a928957)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [w1_rom_to_uint64](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga178a88d0c585d5df0405aadde3ea9178)
- [sys_get_be64](../byteorder_reference/P001_系统字节序头文件参考.md#ad8e00ff5c0b9e394291936d1a570c215)
- [w1_uint64_to_rom](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga6e4dba051a6b29c974e499db17315034)
- [sys_put_be64](../byteorder_reference/P001_系统字节序头文件参考.md#a3e0d2e4e85249497011f5f9ea0d2987c)
- [w1_crc8](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga350a384a6040d1fbb86bfb804013ade3)
- [crc8](../data_utilities/P003_CRC计算接口.md#gaa614e73ee7484ca0424fa7d14a54bbb6)
- [W1_CRC8_POLYNOMIAL](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#gabe56ffbe20c2ba7e0a5c87c8e36c45e5)
- [W1_CRC8_SEED](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#gaa4ad8d9a3791fbca6c99d49b9793a002)
- [w1_crc16](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#ga5635f79a54a2e5b96c8b7ca9a8ab8366)
- [crc16_reflect](../data_utilities/P003_CRC计算接口.md#gaccbcb5b80cf8deaac252474ecc6d9914)
- [W1_CRC16_POLYNOMIAL](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__network.html#gab94362fbf4eec5f115f93fc8976cff0d)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [device::data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [device::config](../device_reference/P002_设备对象结构.md#aca2d801eb15996cf1c74dc65cfa651fc)
- [w1_driver_api::write_block](../peripheral_bus_storage_model_reference/P095_w1_driver_api_结构体.md#a145e07fc821cf21795db761f6c82d650)
- [w1_driver_api::configure](../peripheral_bus_storage_model_reference/P095_w1_driver_api_结构体.md#a1ee0dae9846d2e7ba9a016d3333b040e)
- [w1_driver_api::reset_bus](../peripheral_bus_storage_model_reference/P095_w1_driver_api_结构体.md#a2c3312afc1929fafed6db5607e4f7d2c)
- [w1_driver_api::change_bus_lock](../peripheral_bus_storage_model_reference/P095_w1_driver_api_结构体.md#a34ea6f69f0cc3502a5639f7a5a3c3c1f)
- [w1_driver_api::read_block](../peripheral_bus_storage_model_reference/P095_w1_driver_api_结构体.md#a84f92f1c855550e54a4c5d53e72af5c7)
- [w1_driver_api::write_bit](../peripheral_bus_storage_model_reference/P095_w1_driver_api_结构体.md#ac89908044403cd1d8768425617bd1b86)
- [w1_driver_api::read_bit](../peripheral_bus_storage_model_reference/P095_w1_driver_api_结构体.md#ae7d6cef0458e281c1b653a4e6ecbe3f1)
- [w1_driver_api::write_byte](../peripheral_bus_storage_model_reference/P095_w1_driver_api_结构体.md#ae930e72652123e0f616ed59ebf179f0c)
- [w1_driver_api::read_byte](../peripheral_bus_storage_model_reference/P095_w1_driver_api_结构体.md#aec4d570356600e1c769626d3cb9e75f2)
- [w1_master_config::slave_count](../peripheral_bus_storage_model_reference/P096_w1_master_config_结构体.md#a5cf7b0808d939ad7a6fec4540c36f4c4)
- [w1_master_data::bus_lock](../peripheral_bus_storage_model_reference/P097_w1_master_data_结构体.md#af9cc46f803aff0d5e0d8ca345aaf8b9e)
- [w1_rom::serial](../peripheral_bus_storage_model_reference/P098_w1_rom_结构体.md#a134ee6d6e5e5eb711caf59449d11732e)
- [w1_rom::crc](../peripheral_bus_storage_model_reference/P098_w1_rom_结构体.md#a73d85d7ce0ef671027c910b9b7a54165)
- [w1_rom::family](../peripheral_bus_storage_model_reference/P098_w1_rom_结构体.md#adc7f4f9fca172392b11864a17424a14c)
- [w1_slave_config::rom](../peripheral_bus_storage_model_reference/P099_w1_slave_config_结构体.md#a9f42fd1257483f308115ae02e6ef8596)
- [w1_slave_config::overdrive](../peripheral_bus_storage_model_reference/P099_w1_slave_config_结构体.md#ab8a2d4522505416863fed561df22d058)
- [byteorder.h](../byteorder_reference/P001_系统字节序头文件参考.md)
- [crc.h](../data_utilities/P004_CRC系统头文件.md)

---

[上一章](P028_zephyr__drivers__swdp.h_头文件源码.md) · [返回大纲](大纲.md)
