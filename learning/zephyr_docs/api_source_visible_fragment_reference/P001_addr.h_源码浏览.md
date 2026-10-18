---
id: learning.zephyr-docs.api-source-visible-fragment-reference.page-1
title: addr.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/addr_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_addr.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/addr_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/addr_8h.html)。

## 1.1\_原始可见代码（Source Code）

> 译注：官方源码浏览页保留了部分缺少起始标记的注释尾段。下方代码保持原样；这些可见尾段也逐项翻译，不补写页面中已经省略的注释。

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
<a id="l00041"></a>
<a id="foldopen00042"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="foldopen00051"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
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
<a id="l00067"></a>
<a id="l00069"></a>
<a id="l00071"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="foldopen00078"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="foldopen00088"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
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
<a id="foldopen00115"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="foldopen00125"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="foldopen00135"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="foldopen00146"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00157"></a>
<a id="l00160"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00165"></a>
<a id="l00167"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="foldopen00180"></a>
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
<a id="foldopen00198"></a>
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
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="foldopen00235"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00239"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="foldopen00264"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
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
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00295"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="l00303"></a>
<a id="l00305"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="l00338"></a>
<a id="l00339"></a>
<a id="l00354"></a>
<a id="l00355"></a>
<a id="l00379"></a>
<a id="l00380"></a>
<a id="l00384"></a>
<a id="l00385"></a>
<a id="l00386"></a>
<a id="l00387"></a>
<a id="l00388"></a>
<a id="l00389"></a>
<a id="agroup__bt__addr_html_ga0b2f611fbd28b066d261b81303c4b93f"></a>
<a id="agroup__bt__addr_html_ga0cb3aa4d48cf41d8485b570ef0e7447a"></a>
<a id="agroup__bt__addr_html_ga151bdd0ada8635acfebd60f0e203cde2"></a>
<a id="agroup__bt__addr_html_ga1717d2b4e61b28637be8a5f78685a3c4"></a>
<a id="agroup__bt__addr_html_ga1fd60d5eb4c8a6d8f4df06eaba85fb96"></a>
<a id="agroup__bt__addr_html_ga24752df467449d7cb0dc25e3c4330862"></a>
<a id="agroup__bt__addr_html_ga28baaccd1e89d8939d3a73d759cded09"></a>
<a id="agroup__bt__addr_html_ga32abc1a2e827542efea5b9cb05a57fbc"></a>
<a id="agroup__bt__addr_html_ga40c282f720d13b5d24a2dd62bfdceb73"></a>
<a id="agroup__bt__addr_html_ga41ff9419098728f037c3e97d29c30ba9"></a>
<a id="agroup__bt__addr_html_ga42bcee6b5aadde7ccdbe243df25043bc"></a>
<a id="agroup__bt__addr_html_ga588d392f51372ff2951c3ff39da22f12"></a>
<a id="agroup__bt__addr_html_ga5a8284cf34d0835d725dab31d710ea4c"></a>
<a id="agroup__bt__addr_html_ga6b6f56325b5136d2719f02eecc780d49"></a>
<a id="agroup__bt__addr_html_ga6e81e967527b5418ee6cbc6d72c5aef9"></a>
<a id="agroup__bt__addr_html_ga74a644cd3de081a353a281d80b32b91e"></a>
<a id="agroup__bt__addr_html_ga756d59776902ad1ae2df1c032e91589c"></a>
<a id="agroup__bt__addr_html_ga7a6acc7a9267ae2645aeee38e553b8b3"></a>
<a id="agroup__bt__addr_html_ga8097c3b80a5647b0b951d29aa30a397d"></a>
<a id="agroup__bt__addr_html_ga8644e77108f029088adb203e5392016b"></a>
<a id="agroup__bt__addr_html_gac6c9b20f17936efaa082fe63aedc2138"></a>
<a id="agroup__bt__addr_html_gad1b43f2f0ab58ec2c5ceaaa0d2cbc444"></a>
<a id="agroup__bt__addr_html_gad93410d0161ca84939f4bf983da29c14"></a>
<a id="agroup__bt__addr_html_gadd64afda1a14cbc2740f205e90169152"></a>
<a id="agroup__bt__addr_html_gadecf8fe8e183a11a4ff569bc0d673ec1"></a>
<a id="agroup__bt__addr_html_gae0df0067c55eb4388625bb62f3d7e235"></a>
<a id="agroup__bt__addr_html_gaefa17a553b6f8e9ad599e8db7538e1b8"></a>
<a id="agroup__bt__addr_html_gaf2d38888131c9e8bdbc820b415c14082"></a>
<a id="aprintk_8h_html"></a>
<a id="aprintk_8h_html_a0b0af71688f7e9170103d771d4e1eab2"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astring_8h_html"></a>
<a id="astring_8h_html_ad8bfbfa1e4ad284ded921dd775735521"></a>
<a id="astring_8h_html_af0f01bffcd16daa9143f6014d10a25ad"></a>
<a id="astructbt__addr__le__t_html"></a>
<a id="astructbt__addr__le__t_html_aa4ede005c57893383a21983bc3e47958"></a>
<a id="astructbt__addr__le__t_html_aacada5fc5b04ff22a02518e6f59387ed"></a>
<a id="astructbt__addr__t_html"></a>
<a id="astructbt__addr__t_html_a59e03c3fd06d16dc41132fd21ac42952"></a>

```c


/*
 * Copyright (c) 2019 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_BLUETOOTH_ADDR_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_ADDR_H_

#include <stdint.h>
#include <string.h>

#include <zephyr/sys/printk.h>

#ifdef __cplusplus
extern "C" {
#endif


#define BT_ADDR_LE_PUBLIC       0x00
#define BT_ADDR_LE_RANDOM       0x01
#define BT_ADDR_LE_PUBLIC_ID    0x02
#define BT_ADDR_LE_RANDOM_ID    0x03
#define BT_ADDR_LE_UNRESOLVED   0xFE /* Resolvable Private Address
                                      * (Controller unable to resolve)
                                      */
#define BT_ADDR_LE_ANONYMOUS    0xFF /* No address provided
                                      * (anonymous advertisement)
                                      */

/** Length in bytes of a standard Bluetooth address */
#define BT_ADDR_SIZE 6


typedef struct {
        uint8_t  val[BT_ADDR_SIZE];
} bt_addr_t;
/**/

/** Length in bytes of an LE Bluetooth address. Not packed, so no sizeof() */
#define BT_ADDR_LE_SIZE 7

typedef struct {
        uint8_t      type;
        bt_addr_t a;
} bt_addr_le_t;

/* Global Bluetooth address constants defined in bluetooth/common/addr.c */
extern const bt_addr_t bt_addr_any;
extern const bt_addr_t bt_addr_none;
extern const bt_addr_le_t bt_addr_le_any;
extern const bt_addr_le_t bt_addr_le_none;

#define BT_ADDR_ANY     (&bt_addr_any)
#define BT_ADDR_NONE    (&bt_addr_none)
#define BT_ADDR_LE_ANY  (&bt_addr_le_any)
#define BT_ADDR_LE_NONE (&bt_addr_le_none)

 *  @param b Second Bluetooth device address to compare
 *
 *  @return negative value if @a a < @a b, 0 if @a a == @a b, else positive
 */
static inline int bt_addr_cmp(const bt_addr_t *a, const bt_addr_t *b)
{
        return memcmp(a, b, sizeof(*a));
}

 *
 *  @retval true if the two addresses are equal
 *  @retval false otherwise
 */
static inline bool bt_addr_eq(const bt_addr_t *a, const bt_addr_t *b)
{
        return bt_addr_cmp(a, b) == 0;
}

 *  @return negative value if @a a < @a b, 0 if @a a == @a b, else positive
 *
 *  @sa bt_addr_le_eq
 */
static inline int bt_addr_le_cmp(const bt_addr_le_t *a, const bt_addr_le_t *b)
{
        return memcmp(a, b, sizeof(*a));
}

 *
 *  @retval true if the two addresses are equal
 *  @retval false otherwise
 */
static inline bool bt_addr_le_eq(const bt_addr_le_t *a, const bt_addr_le_t *b)
{
        return bt_addr_le_cmp(a, b) == 0;
}

 *
 *  @param dst Bluetooth device address destination buffer.
 *  @param src Bluetooth device address source buffer.
 */
static inline void bt_addr_copy(bt_addr_t *dst, const bt_addr_t *src)
{
        memcpy(dst, src, sizeof(*dst));
}

 *
 *  @param dst Bluetooth LE device address destination buffer.
 *  @param src Bluetooth LE device address source buffer.
 */
static inline void bt_addr_le_copy(bt_addr_le_t *dst, const bt_addr_le_t *src)
{
        memcpy(dst, src, sizeof(*dst));
}

 *  @param dst Bluetooth LE device address destination buffer.
 *  @param src Bluetooth device address source buffer.
 *  @param src_type Bluetooth device address source type.
 */
static inline void bt_addr_le_copy_addr(bt_addr_le_t *dst, const bt_addr_t *src, uint8_t src_type)
{
        bt_addr_copy(&dst->a, src);
        dst->type = src_type;
}

#define BT_ADDR_IS_RPA(a)     (((a)->val[5] & 0xc0) == 0x40)
#define BT_ADDR_IS_NRPA(a)    (((a)->val[5] & 0xc0) == 0x00)
#define BT_ADDR_IS_STATIC(a)  (((a)->val[5] & 0xc0) == 0xc0)

#define BT_ADDR_SET_RPA(a)    ((a)->val[5] = (((a)->val[5] & 0x3f) | 0x40))
#define BT_ADDR_SET_NRPA(a)   ((a)->val[5] &= 0x3f)
#define BT_ADDR_SET_STATIC(a) ((a)->val[5] |= 0xc0)

int bt_addr_le_create_nrpa(bt_addr_le_t *addr);

int bt_addr_le_create_static(bt_addr_le_t *addr);

 *  @param addr Bluetooth LE device address.
 *
 *  @return true if address is a random private resolvable address.
 */
static inline bool bt_addr_le_is_rpa(const bt_addr_le_t *addr)
{
        if (addr->type != BT_ADDR_LE_RANDOM) {
                return false;
        }

        return BT_ADDR_IS_RPA(&addr->a);
}

 *  @param addr Bluetooth LE device address.
 *
 *  @return true if address is a valid identity address.
 */
static inline bool bt_addr_le_is_identity(const bt_addr_le_t *addr)
{
        if (addr->type == BT_ADDR_LE_PUBLIC) {
                return true;
        }

        return BT_ADDR_IS_STATIC(&addr->a);
}

#define BT_ADDR_STR_LEN 18

#define BT_ADDR_LE_STR_LEN 20

 *  BT_ADDR_STR_LEN about recommended value.
 *
 *  @return Number of successfully formatted bytes from binary address.
 */
static inline int bt_addr_to_str(const bt_addr_t *addr, char *str, size_t len)
{
        return snprintk(str, len, "%02X:%02X:%02X:%02X:%02X:%02X",
                        addr->val[5], addr->val[4], addr->val[3],
                        addr->val[2], addr->val[1], addr->val[0]);
}

 *  BT_ADDR_LE_STR_LEN about recommended value.
 *
 *  @return Number of successfully formatted bytes from binary address.
 */
static inline int bt_addr_le_to_str(const bt_addr_le_t *addr, char *str,
                                    size_t len)
{
        char type_char;

        switch (addr->type) {
        case BT_ADDR_LE_PUBLIC:
        case BT_ADDR_LE_PUBLIC_ID:
                type_char = 'P';
                break;
        default:
                /* BT_ADDR_LE_RANDOM, BT_ADDR_LE_RANDOM_ID and the unresolved-RPA
                 * and anonymous sentinels, none of which are public addresses.
                 */
                type_char = 'R';
                break;
        }

        return snprintk(str, len, "%c:%02X:%02X:%02X:%02X:%02X:%02X",
                        type_char,
                        addr->a.val[5], addr->a.val[4], addr->a.val[3],
                        addr->a.val[2], addr->a.val[1], addr->a.val[0]);
}

struct bt_addr_tmp_str {
        char str[BT_ADDR_STR_LEN];
};

struct bt_addr_tmp_str bt_addr_tmp_str(const bt_addr_t *addr);

struct bt_addr_le_tmp_str {
        char str[BT_ADDR_LE_STR_LEN];
};

struct bt_addr_le_tmp_str bt_addr_le_tmp_str(const bt_addr_le_t *addr);

#define bt_addr_str(_addr) bt_addr_tmp_str(_addr).str

#define bt_addr_le_str(_addr) bt_addr_le_tmp_str(_addr).str

int bt_addr_from_str(const char *str, bt_addr_t *addr);

int bt_addr_le_from_str(const char *str, bt_addr_le_t *addr);

int bt_addr_le_rpa_resolve(uint8_t id, const bt_addr_le_t *addr, bt_addr_le_t *resolved_addr);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_ADDR_H_ */
```

## 1.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权所有（Copyright）2019 Nordic Semiconductor ASA。

SPDX-License-Identifier: Apache-2.0。

### 注释 2：原第 35 行

可解析私有地址（Resolvable Private Address），但控制器（Controller）无法解析。

### 注释 3：原第 38 行

未提供地址（No Address Provided），用于匿名广播（Anonymous Advertisement）。

### 注释 4：原第 42 行

标准蓝牙地址（Standard Bluetooth Address）的长度，单位为字节（Bytes）。

### 注释 5：原第 49 行

空注释，无需翻译。

### 注释 6：原第 51 行

低功耗蓝牙地址（LE Bluetooth Address）的长度，单位为字节（Bytes）。该结构未采用紧凑布局（Not Packed），因此不能使用 `sizeof()` 确定此长度。

### 注释 7：原第 60 行

在 `bluetooth/common/addr.c` 中定义的全局蓝牙地址常量（Global Bluetooth Address Constants）。

### 注释 8：原第 78 行

参数（`@param`）`b`：参与比较的第二个蓝牙设备地址（Bluetooth Device Address）。

返回（`@return`）：若 `a < b` 则返回负值，若 `a == b` 则返回 0，否则返回正值。

### 注释 9：原第 88 行

返回值（`@retval`）：两个地址相等时为 `true`；否则为 `false`。

### 注释 10：原第 102 行

返回（`@return`）：若 `a < b` 则返回负值，若 `a == b` 则返回 0，否则返回正值。

另请参见（`@sa`）`bt_addr_le_eq`。

### 注释 11：原第 115 行

返回值（`@retval`）：两个地址相等时为 `true`；否则为 `false`。

### 注释 12：原第 125 行

参数（`@param`）`dst`：蓝牙设备地址目标缓冲区（Destination Buffer）。

参数（`@param`）`src`：蓝牙设备地址源缓冲区（Source Buffer）。

### 注释 13：原第 135 行

参数（`@param`）`dst`：低功耗蓝牙设备地址目标缓冲区（Bluetooth LE Device Address Destination Buffer）。

参数（`@param`）`src`：低功耗蓝牙设备地址源缓冲区（Source Buffer）。

### 注释 14：原第 146 行

参数（`@param`）`dst`：低功耗蓝牙设备地址目标缓冲区（Bluetooth LE Device Address Destination Buffer）。

参数（`@param`）`src`：蓝牙设备地址源缓冲区（Source Buffer）。

参数（`@param`）`src_type`：蓝牙设备地址源类型（Source Type）。

### 注释 15：原第 180 行

参数（`@param`）`addr`：低功耗蓝牙设备地址（Bluetooth LE Device Address）。

返回（`@return`）：若地址为随机可解析私有地址（Random Private Resolvable Address），则返回 `true`。

### 注释 16：原第 198 行

参数（`@param`）`addr`：低功耗蓝牙设备地址（Bluetooth LE Device Address）。

返回（`@return`）：若地址为有效身份地址（Valid Identity Address），则返回 `true`。

### 注释 17：原第 235 行

建议取值（Recommended Value）参见 `BT_ADDR_STR_LEN`。

返回（`@return`）：成功从二进制地址（Binary Address）格式化出的字节数。

### 注释 18：原第 264 行

建议取值（Recommended Value）参见 `BT_ADDR_LE_STR_LEN`。

返回（`@return`）：成功从二进制地址（Binary Address）格式化出的字节数。

### 注释 19：原第 279 行

`BT_ADDR_LE_RANDOM`、`BT_ADDR_LE_RANDOM_ID`，以及未解析的可解析私有地址（Unresolved RPA）哨兵值和匿名哨兵值（Anonymous Sentinel），都不是公共地址（Public Addresses）。

### 注释 20：原第 389 行

头文件包含保护（Include Guard）：`ZEPHYR_INCLUDE_BLUETOOTH_ADDR_H_`。

## 1.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/addr_8h.html)
- [stdint.h](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md)
- [string.h](../api_file_reference/P472_____w__zephyr__zephyr__lib__libc__minimal__include__string.h_文件参考.md)
- [zephyr/sys/printk.h](https://docs.zephyrproject.org/latest/doxygen/html/printk_8h.html)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [val](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md#a59e03c3fd06d16dc41132fd21ac42952)
- [BT_ADDR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga6b6f56325b5136d2719f02eecc780d49)
- [bt_addr_t](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md)
- [type](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md#aa4ede005c57893383a21983bc3e47958)
- [a](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md#aacada5fc5b04ff22a02518e6f59387ed)
- [bt_addr_le_t](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md)
- [bt_addr_any](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#gadd64afda1a14cbc2740f205e90169152)
- [bt_addr_none](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga0b2f611fbd28b066d261b81303c4b93f)
- [bt_addr_le_any](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga40c282f720d13b5d24a2dd62bfdceb73)
- [bt_addr_le_none](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#gaefa17a553b6f8e9ad599e8db7538e1b8)
- [bt_addr_cmp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga41ff9419098728f037c3e97d29c30ba9)
- [memcmp](../api_file_reference/P472_____w__zephyr__zephyr__lib__libc__minimal__include__string.h_文件参考.md#ad8bfbfa1e4ad284ded921dd775735521)
- [bt_addr_eq](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#gadecf8fe8e183a11a4ff569bc0d673ec1)
- [bt_addr_le_cmp](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga588d392f51372ff2951c3ff39da22f12)
- [bt_addr_le_eq](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga8644e77108f029088adb203e5392016b)
- [bt_addr_copy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga5a8284cf34d0835d725dab31d710ea4c)
- [memcpy](../api_file_reference/P472_____w__zephyr__zephyr__lib__libc__minimal__include__string.h_文件参考.md#af0f01bffcd16daa9143f6014d10a25ad)
- [bt_addr_le_copy](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#gac6c9b20f17936efaa082fe63aedc2138)
- [bt_addr_le_copy_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga756d59776902ad1ae2df1c032e91589c)
- [bt_addr_le_create_nrpa](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#gaf2d38888131c9e8bdbc820b415c14082)
- [bt_addr_le_create_static](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#gad1b43f2f0ab58ec2c5ceaaa0d2cbc444)
- [bt_addr_le_is_rpa](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga42bcee6b5aadde7ccdbe243df25043bc)
- [BT_ADDR_LE_RANDOM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga6e81e967527b5418ee6cbc6d72c5aef9)
- [BT_ADDR_IS_RPA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga32abc1a2e827542efea5b9cb05a57fbc)
- [bt_addr_le_is_identity](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga7a6acc7a9267ae2645aeee38e553b8b3)
- [BT_ADDR_LE_PUBLIC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga1717d2b4e61b28637be8a5f78685a3c4)
- [BT_ADDR_IS_STATIC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga0cb3aa4d48cf41d8485b570ef0e7447a)
- [bt_addr_to_str](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga151bdd0ada8635acfebd60f0e203cde2)
- [snprintk](https://docs.zephyrproject.org/latest/doxygen/html/printk_8h.html#a0b0af71688f7e9170103d771d4e1eab2)
- [bt_addr_le_to_str](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga74a644cd3de081a353a281d80b32b91e)
- [BT_ADDR_LE_PUBLIC_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga1fd60d5eb4c8a6d8f4df06eaba85fb96)
- [BT_ADDR_STR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga8097c3b80a5647b0b951d29aa30a397d)
- [BT_ADDR_LE_STR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#gae0df0067c55eb4388625bb62f3d7e235)
- [bt_addr_from_str](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#gad93410d0161ca84939f4bf983da29c14)
- [bt_addr_le_from_str](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga24752df467449d7cb0dc25e3c4330862)
- [bt_addr_le_rpa_resolve](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html#ga28baaccd1e89d8939d3a73d759cded09)
- [printk.h](https://docs.zephyrproject.org/latest/doxygen/html/printk_8h.html)
- [bt_addr_le_t::type](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md#aa4ede005c57893383a21983bc3e47958)
- [bt_addr_le_t::a](../bluetooth_classic_model_reference/P011_bt_addr_le_t_结构体.md#aacada5fc5b04ff22a02518e6f59387ed)
- [bt_addr_t::val](../bluetooth_classic_model_reference/P012_bt_addr_t_结构体.md#a59e03c3fd06d16dc41132fd21ac42952)

---

[返回大纲](大纲.md) · [下一章](P002_gpio_bl61x_wo.h_源码浏览.md)
