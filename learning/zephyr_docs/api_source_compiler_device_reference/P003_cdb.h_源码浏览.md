---
id: learning.zephyr-docs.api-source-compiler-device-reference.page-3
title: cdb.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_cdb.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html)。

## 3.1\_原始可见代码（Source Code）

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
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
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
<a id="l00041"></a>
<a id="l00042"></a>
<a id="foldopen00043"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="foldopen00060"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="foldopen00073"></a>
<a id="l00073"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="l00079"></a>
<a id="l00080"></a>
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
<a id="foldopen00096"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00100"></a>
<a id="l00102"></a>
<a id="l00104"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00303"></a>
<a id="l00304"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00333"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00350"></a>
<a id="l00351"></a>
<a id="l00352"></a>
<a id="l00363"></a>
<a id="l00364"></a>
<a id="l00365"></a>
<a id="l00373"></a>
<a id="l00374"></a>
<a id="l00384"></a>
<a id="l00385"></a>
<a id="l00390"></a>
<a id="l00391"></a>
<a id="l00406"></a>
<a id="l00407"></a>
<a id="l00422"></a>
<a id="l00423"></a>
<a id="l00424"></a>
<a id="l00425"></a>
<a id="l00426"></a>
<a id="l00427"></a>
<a id="l00428"></a>
<a id="aatomic_8h_html"></a>
<a id="acdb_8h_html_a00490e69b96e88cdf7336ca22e63617d"></a>
<a id="acdb_8h_html_a0e45ffdd001e9fac31b74949a004e8f5a229d9bfcc277ea2cb81e991a1a30ceb6"></a>
<a id="acdb_8h_html_a0e45ffdd001e9fac31b74949a004e8f5a3fe59a5bb698f65be4389345fe63ccc1"></a>
<a id="acdb_8h_html_a0e45ffdd001e9fac31b74949a004e8f5a5d07a0f33a2544be141d1fb4c6130bdd"></a>
<a id="acdb_8h_html_a0e45ffdd001e9fac31b74949a004e8f5a62fc7baf49a7bf92a3b3c80eb57d8cf8"></a>
<a id="acdb_8h_html_a0e45ffdd001e9fac31b74949a004e8f5abf303893a5d3b399856b3670c4a7fd41"></a>
<a id="acdb_8h_html_a0e45ffdd001e9fac31b74949a004e8f5ad5a2fc5c15efc200ef31b8876eabc01d"></a>
<a id="acdb_8h_html_a121a30fd546ccb887c2c49ceef65c2d6"></a>
<a id="acdb_8h_html_a159f4eec3bbcaed25a4369b67e6937f1a00449c6d1403f903b115c3de36a2a3bd"></a>
<a id="acdb_8h_html_a159f4eec3bbcaed25a4369b67e6937f1aab4ca02f1d0d9f6a743bee9f66eeba12"></a>
<a id="acdb_8h_html_a26b1e5560998cc37e2a627c44326db62"></a>
<a id="acdb_8h_html_a2ec5612f827a95662f18bc9e012048cda6b057da4bd763f7c65e41410b7c72218"></a>
<a id="acdb_8h_html_a2ec5612f827a95662f18bc9e012048cdaf2362ea16e4733a32e26138a3577e5fb"></a>
<a id="acdb_8h_html_a34dcf031e675235cdcbe0e1f76c00cf3"></a>
<a id="acdb_8h_html_a3d0034ec500d3964dd4b428e518abfb9"></a>
<a id="acdb_8h_html_a4a0f7577f1a8df96e4dcab6f682abf23"></a>
<a id="acdb_8h_html_a4bf4f49fbd75ee33876ffd34f6c6f76f"></a>
<a id="acdb_8h_html_a4e9470adfa797be85b7f4df43b63d6d2"></a>
<a id="acdb_8h_html_a59e6b7da8c91df35ce6f8268da35c933"></a>
<a id="acdb_8h_html_a5ab07a907049974c089a4b0dd706ef77"></a>
<a id="acdb_8h_html_a5d00af9f4c971f31c3016824757ebf66"></a>
<a id="acdb_8h_html_a66df2f6b6363af595181fe722122996d"></a>
<a id="acdb_8h_html_a692c6980c9b0d2da18e8f47d67757f07"></a>
<a id="acdb_8h_html_a6d9cc2d360075b6b3e939a4979e08895"></a>
<a id="acdb_8h_html_a87cfce7316efabe4c8b24be6c3b6d8b4"></a>
<a id="acdb_8h_html_a9ad0651ccaa7ff1f86402ce8c05c9410"></a>
<a id="acdb_8h_html_aa10c4ec973e61626ba6424e443fb0b88"></a>
<a id="acdb_8h_html_aa6d124339002c43fc35f301a9eef3e7c"></a>
<a id="acdb_8h_html_aab65f293c17c657d670e802bbfe389d7"></a>
<a id="acdb_8h_html_ab0dc86dd674f57a820aa3f5cebf77895"></a>
<a id="acdb_8h_html_ab728a20fdb1535cc7059a39e8490a736"></a>
<a id="acdb_8h_html_ab82dcdf26d66ea4ab0df34bc23421f39"></a>
<a id="acdb_8h_html_aba737b508e0e40dfb5ad9da9d7b6fd11"></a>
<a id="acdb_8h_html_ac361a17a704195e852faecda09881203"></a>
<a id="acdb_8h_html_ac775f3d1be745aeba2979b9ae4b42c4f"></a>
<a id="acdb_8h_html_ad4333e02b866589f7ca2b155cf814ca4"></a>
<a id="acdb_8h_html_ae49e5e1ae89eef30538ae9f45c772b64"></a>
<a id="acdb_8h_html_ae8ed0ef1a00e973d864c944c9d9400bc"></a>
<a id="acdb_8h_html_aeba4ed506e30ab8d91746b36e7e5f968"></a>
<a id="agroup__atomic__apis_html_ga249c575db9764486197709b327f7370e"></a>
<a id="amesh_8h_html"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructbt__mesh__cdb__app__key_html"></a>
<a id="astructbt__mesh__cdb__app__key_html_a2d685a7dd5e1f4678c34ea72be3fe6a2"></a>
<a id="astructbt__mesh__cdb__app__key_html_a2ef7f5d832b36736d3a1811a407b6fa6"></a>
<a id="astructbt__mesh__cdb__app__key_html_aa113eaa2a648cdabe21dc2c57b31bf65"></a>
<a id="astructbt__mesh__cdb__app__key_html_afa234a0d5f0fb61513a97afb91986976"></a>
<a id="astructbt__mesh__cdb__node_html"></a>
<a id="astructbt__mesh__cdb__node_html_a2313e29b756344a493989f39ba1ec726"></a>
<a id="astructbt__mesh__cdb__node_html_a32f48db827713e53e02c0c1574476835"></a>
<a id="astructbt__mesh__cdb__node_html_a54e5130d7dabedf09e23419a40f6778b"></a>
<a id="astructbt__mesh__cdb__node_html_a751671f52c4fdf3f42b6f71193976dd5"></a>
<a id="astructbt__mesh__cdb__node_html_a8c9941929a8ce6228817d76fe4e2375c"></a>
<a id="astructbt__mesh__cdb__node_html_aa936534676ef7e256670d356eff7ac17"></a>
<a id="astructbt__mesh__cdb__subnet_html"></a>
<a id="astructbt__mesh__cdb__subnet_html_a07fbd0e52571cd9a16e876243483e98a"></a>
<a id="astructbt__mesh__cdb__subnet_html_a1010965e2030e1bef181920fc5f76116"></a>
<a id="astructbt__mesh__cdb__subnet_html_a2f04c34ebbb8ae1e33f6679f94690c9a"></a>
<a id="astructbt__mesh__cdb__subnet_html_a40d47a7705f4d3a9ba9349972d11072a"></a>
<a id="astructbt__mesh__cdb_html"></a>
<a id="astructbt__mesh__cdb_html_a48b3cf852a42b580f911e193a9764517"></a>
<a id="astructbt__mesh__cdb_html_a59a130ffed26c362dc72d57d1ac7d7fd"></a>
<a id="astructbt__mesh__cdb_html_a7af2ac65c8919c594b8283ff57b5b7fc"></a>
<a id="astructbt__mesh__cdb_html_aa2526502debab1add405fe6e2c475475"></a>
<a id="astructbt__mesh__cdb_html_acb7f3ae85a5929b9cfc18531e1d98ab5"></a>
<a id="astructbt__mesh__cdb_html_ae391c898d11257c484c4e8d1b38fd9dc"></a>
<a id="astructbt__mesh__key_html"></a>
<a id="astructuuid_html"></a>

```c
/*
 * Copyright (c) 2019 Tobias Svehagen
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_BLUETOOTH_MESH_CDB_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_MESH_CDB_H_

#include <stdbool.h>
#include <stdint.h>

#include <zephyr/sys/atomic.h>
#include <zephyr/bluetooth/mesh.h>

#ifdef __cplusplus
extern "C" {
#endif

#if defined(CONFIG_BT_MESH_CDB)
#define NODE_COUNT    CONFIG_BT_MESH_CDB_NODE_COUNT
#define SUBNET_COUNT  CONFIG_BT_MESH_CDB_SUBNET_COUNT
#define APP_KEY_COUNT CONFIG_BT_MESH_CDB_APP_KEY_COUNT
#else
#define NODE_COUNT    0
#define SUBNET_COUNT  0
#define APP_KEY_COUNT 0
#endif

enum {
        BT_MESH_CDB_NODE_CONFIGURED,

        BT_MESH_CDB_NODE_FLAG_COUNT
};

/* doc string cdb node start */
struct bt_mesh_cdb_node {
        uint8_t  uuid[16];
        uint16_t addr;
        uint16_t net_idx;
        uint8_t  num_elem;
        struct bt_mesh_key dev_key;
        ATOMIC_DEFINE(flags, BT_MESH_CDB_NODE_FLAG_COUNT);
};
/* doc string cdb node end */

/* doc string cdb subnet start */
struct bt_mesh_cdb_subnet {
        uint16_t net_idx;
        uint8_t kr_phase;
        struct {
                struct bt_mesh_key net_key;
        } keys[2];
};
/* doc string cdb subnet end */

/* doc string cdb app key start */
struct bt_mesh_cdb_app_key {
        uint16_t net_idx;
        uint16_t app_idx;
        struct {
                struct bt_mesh_key app_key;
        } keys[2];
};
/* doc string cdb app key end */

enum {
        BT_MESH_CDB_VALID,
        BT_MESH_CDB_SUBNET_PENDING,
        BT_MESH_CDB_KEYS_PENDING,
        BT_MESH_CDB_NODES_PENDING,
        BT_MESH_CDB_IVU_IN_PROGRESS,

        BT_MESH_CDB_FLAG_COUNT,
};

/* doc string cdb start */
struct bt_mesh_cdb {
        uint32_t iv_index;
        uint16_t lowest_avail_addr;
        ATOMIC_DEFINE(flags, BT_MESH_CDB_FLAG_COUNT);
        struct bt_mesh_cdb_node nodes[NODE_COUNT];
        struct bt_mesh_cdb_subnet subnets[SUBNET_COUNT];
        struct bt_mesh_cdb_app_key app_keys[APP_KEY_COUNT];
};

extern struct bt_mesh_cdb bt_mesh_cdb;
/* doc string cdb end */

int bt_mesh_cdb_create(const uint8_t key[16]);

void bt_mesh_cdb_clear(void);

void bt_mesh_cdb_iv_update(uint32_t iv_index, bool iv_update);

struct bt_mesh_cdb_node *bt_mesh_cdb_node_alloc(const uint8_t uuid[16], uint16_t addr,
                                                uint8_t num_elem, uint16_t net_idx);

uint16_t bt_mesh_cdb_free_addr_get(uint8_t num_elem);

void bt_mesh_cdb_node_del(struct bt_mesh_cdb_node *node, bool store);

void bt_mesh_cdb_node_update(struct bt_mesh_cdb_node *node, uint16_t addr,
                             uint8_t num_elem);

struct bt_mesh_cdb_node *bt_mesh_cdb_node_get(uint16_t addr);

void bt_mesh_cdb_node_store(const struct bt_mesh_cdb_node *node);

int bt_mesh_cdb_node_key_import(struct bt_mesh_cdb_node *node, const uint8_t in[16]);

int bt_mesh_cdb_node_key_export(const struct bt_mesh_cdb_node *node, uint8_t out[16]);

enum {
        BT_MESH_CDB_ITER_STOP = 0,
        BT_MESH_CDB_ITER_CONTINUE,
};

typedef uint8_t (*bt_mesh_cdb_node_func_t)(struct bt_mesh_cdb_node *node,
                                           void *user_data);

void bt_mesh_cdb_node_foreach(bt_mesh_cdb_node_func_t func, void *user_data);

struct bt_mesh_cdb_subnet *bt_mesh_cdb_subnet_alloc(uint16_t net_idx);

void bt_mesh_cdb_subnet_del(struct bt_mesh_cdb_subnet *sub, bool store);

struct bt_mesh_cdb_subnet *bt_mesh_cdb_subnet_get(uint16_t net_idx);

void bt_mesh_cdb_subnet_store(const struct bt_mesh_cdb_subnet *sub);

uint8_t bt_mesh_cdb_subnet_flags(const struct bt_mesh_cdb_subnet *sub);

int bt_mesh_cdb_subnet_key_import(struct bt_mesh_cdb_subnet *sub, int key_idx,
                                  const uint8_t in[16]);

int bt_mesh_cdb_subnet_key_export(const struct bt_mesh_cdb_subnet *sub, int key_idx,
                                  uint8_t out[16]);

struct bt_mesh_cdb_app_key *bt_mesh_cdb_app_key_alloc(uint16_t net_idx,
                                                      uint16_t app_idx);

void bt_mesh_cdb_app_key_del(struct bt_mesh_cdb_app_key *key, bool store);

struct bt_mesh_cdb_app_key *bt_mesh_cdb_app_key_get(uint16_t app_idx);

void bt_mesh_cdb_app_key_store(const struct bt_mesh_cdb_app_key *key);

int bt_mesh_cdb_app_key_import(struct bt_mesh_cdb_app_key *key, int key_idx, const uint8_t in[16]);

int bt_mesh_cdb_app_key_export(const struct bt_mesh_cdb_app_key *key, int key_idx, uint8_t out[16]);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_MESH_CDB_H_ */
```

## 3.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2019 Tobias Svehagen。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 42 行

配置数据库（CDB）节点文档字符串开始标记。

### 注释 3：原第 57 行

配置数据库（CDB）节点文档字符串结束标记。

### 注释 4：原第 59 行

配置数据库（CDB）子网文档字符串开始标记。

### 注释 5：原第 70 行

配置数据库（CDB）子网文档字符串结束标记。

### 注释 6：原第 72 行

配置数据库（CDB）应用密钥文档字符串开始标记。

### 注释 7：原第 83 行

配置数据库（CDB）应用密钥文档字符串结束标记。

### 注释 8：原第 95 行

配置数据库（CDB）文档字符串开始标记。

### 注释 9：原第 113 行

配置数据库（CDB）文档字符串结束标记。

### 注释 10：原第 428 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_MESH_CDB_H_`。

## 3.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html)
- [stdbool.h](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md)
- [stdint.h](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md)
- [zephyr/sys/atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [zephyr/bluetooth/mesh.h](../api_file_reference/P218_zephyr__bluetooth__mesh.h_文件参考.md)
- [BT_MESH_CDB_NODE_CONFIGURED](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#a159f4eec3bbcaed25a4369b67e6937f1aab4ca02f1d0d9f6a743bee9f66eeba12)
- [BT_MESH_CDB_NODE_FLAG_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#a159f4eec3bbcaed25a4369b67e6937f1a00449c6d1403f903b115c3de36a2a3bd)
- [bt_mesh_cdb_node](../bluetooth_mesh_model_reference/P025_bt_mesh_cdb_node_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uuid](../bluetooth_mesh_model_reference/P025_bt_mesh_cdb_node_结构体.md#a751671f52c4fdf3f42b6f71193976dd5)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [addr](../bluetooth_mesh_model_reference/P025_bt_mesh_cdb_node_结构体.md#a8c9941929a8ce6228817d76fe4e2375c)
- [net_idx](../bluetooth_mesh_model_reference/P025_bt_mesh_cdb_node_结构体.md#aa936534676ef7e256670d356eff7ac17)
- [num_elem](../bluetooth_mesh_model_reference/P025_bt_mesh_cdb_node_结构体.md#a2313e29b756344a493989f39ba1ec726)
- [bt_mesh_key](../bluetooth_mesh_model_reference/P068_bt_mesh_key_结构体.md)
- [dev_key](../bluetooth_mesh_model_reference/P025_bt_mesh_cdb_node_结构体.md#a54e5130d7dabedf09e23419a40f6778b)
- [ATOMIC_DEFINE](../atomic_reference/P001_原子操作公共接口.md#ga249c575db9764486197709b327f7370e)
- [flags](../bluetooth_mesh_model_reference/P025_bt_mesh_cdb_node_结构体.md#a32f48db827713e53e02c0c1574476835)
- [bt_mesh_cdb_subnet](../bluetooth_mesh_model_reference/P026_bt_mesh_cdb_subnet_结构体.md)
- [net_idx](../bluetooth_mesh_model_reference/P026_bt_mesh_cdb_subnet_结构体.md#a1010965e2030e1bef181920fc5f76116)
- [kr_phase](../bluetooth_mesh_model_reference/P026_bt_mesh_cdb_subnet_结构体.md#a07fbd0e52571cd9a16e876243483e98a)
- [net_key](../bluetooth_mesh_model_reference/P026_bt_mesh_cdb_subnet_结构体.md#a40d47a7705f4d3a9ba9349972d11072a)
- [keys](../bluetooth_mesh_model_reference/P026_bt_mesh_cdb_subnet_结构体.md#a2f04c34ebbb8ae1e33f6679f94690c9a)
- [bt_mesh_cdb_app_key](../bluetooth_mesh_model_reference/P024_bt_mesh_cdb_app_key_结构体.md)
- [net_idx](../bluetooth_mesh_model_reference/P024_bt_mesh_cdb_app_key_结构体.md#afa234a0d5f0fb61513a97afb91986976)
- [app_idx](../bluetooth_mesh_model_reference/P024_bt_mesh_cdb_app_key_结构体.md#a2ef7f5d832b36736d3a1811a407b6fa6)
- [app_key](../bluetooth_mesh_model_reference/P024_bt_mesh_cdb_app_key_结构体.md#a2d685a7dd5e1f4678c34ea72be3fe6a2)
- [keys](../bluetooth_mesh_model_reference/P024_bt_mesh_cdb_app_key_结构体.md#aa113eaa2a648cdabe21dc2c57b31bf65)
- [BT_MESH_CDB_VALID](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#a0e45ffdd001e9fac31b74949a004e8f5ad5a2fc5c15efc200ef31b8876eabc01d)
- [BT_MESH_CDB_SUBNET_PENDING](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#a0e45ffdd001e9fac31b74949a004e8f5a5d07a0f33a2544be141d1fb4c6130bdd)
- [BT_MESH_CDB_KEYS_PENDING](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#a0e45ffdd001e9fac31b74949a004e8f5a62fc7baf49a7bf92a3b3c80eb57d8cf8)
- [BT_MESH_CDB_NODES_PENDING](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#a0e45ffdd001e9fac31b74949a004e8f5a3fe59a5bb698f65be4389345fe63ccc1)
- [BT_MESH_CDB_IVU_IN_PROGRESS](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#a0e45ffdd001e9fac31b74949a004e8f5a229d9bfcc277ea2cb81e991a1a30ceb6)
- [BT_MESH_CDB_FLAG_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#a0e45ffdd001e9fac31b74949a004e8f5abf303893a5d3b399856b3670c4a7fd41)
- [bt_mesh_cdb](../bluetooth_mesh_model_reference/P023_bt_mesh_cdb_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [iv_index](../bluetooth_mesh_model_reference/P023_bt_mesh_cdb_结构体.md#a48b3cf852a42b580f911e193a9764517)
- [lowest_avail_addr](../bluetooth_mesh_model_reference/P023_bt_mesh_cdb_结构体.md#acb7f3ae85a5929b9cfc18531e1d98ab5)
- [flags](../bluetooth_mesh_model_reference/P023_bt_mesh_cdb_结构体.md#aa2526502debab1add405fe6e2c475475)
- [nodes](../bluetooth_mesh_model_reference/P023_bt_mesh_cdb_结构体.md#a7af2ac65c8919c594b8283ff57b5b7fc)
- [NODE_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#ae49e5e1ae89eef30538ae9f45c772b64)
- [subnets](../bluetooth_mesh_model_reference/P023_bt_mesh_cdb_结构体.md#ae391c898d11257c484c4e8d1b38fd9dc)
- [SUBNET_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#a5ab07a907049974c089a4b0dd706ef77)
- [app_keys](../bluetooth_mesh_model_reference/P023_bt_mesh_cdb_结构体.md#a59a130ffed26c362dc72d57d1ac7d7fd)
- [APP_KEY_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#aab65f293c17c657d670e802bbfe389d7)
- [bt_mesh_cdb_create](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#a00490e69b96e88cdf7336ca22e63617d)
- [bt_mesh_cdb_clear](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#a4bf4f49fbd75ee33876ffd34f6c6f76f)
- [bt_mesh_cdb_iv_update](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#aa6d124339002c43fc35f301a9eef3e7c)
- [bt_mesh_cdb_node_alloc](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#ab0dc86dd674f57a820aa3f5cebf77895)
- [uuid](../data_utilities/P026_UUID二进制结构.md)
- [bt_mesh_cdb_free_addr_get](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#aa10c4ec973e61626ba6424e443fb0b88)
- [bt_mesh_cdb_node_del](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#a6d9cc2d360075b6b3e939a4979e08895)
- [bt_mesh_cdb_node_update](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#ad4333e02b866589f7ca2b155cf814ca4)
- [bt_mesh_cdb_node_get](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#a3d0034ec500d3964dd4b428e518abfb9)
- [bt_mesh_cdb_node_store](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#ac775f3d1be745aeba2979b9ae4b42c4f)
- [bt_mesh_cdb_node_key_import](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#a26b1e5560998cc37e2a627c44326db62)
- [bt_mesh_cdb_node_key_export](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#a4a0f7577f1a8df96e4dcab6f682abf23)
- [BT_MESH_CDB_ITER_STOP](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#a2ec5612f827a95662f18bc9e012048cdaf2362ea16e4733a32e26138a3577e5fb)
- [BT_MESH_CDB_ITER_CONTINUE](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#a2ec5612f827a95662f18bc9e012048cda6b057da4bd763f7c65e41410b7c72218)
- [bt_mesh_cdb_node_func_t](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#a5d00af9f4c971f31c3016824757ebf66)
- [bt_mesh_cdb_node_foreach](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#ae8ed0ef1a00e973d864c944c9d9400bc)
- [bt_mesh_cdb_subnet_alloc](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#aeba4ed506e30ab8d91746b36e7e5f968)
- [bt_mesh_cdb_subnet_del](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#a66df2f6b6363af595181fe722122996d)
- [bt_mesh_cdb_subnet_get](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#a34dcf031e675235cdcbe0e1f76c00cf3)
- [bt_mesh_cdb_subnet_store](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#a59e6b7da8c91df35ce6f8268da35c933)
- [bt_mesh_cdb_subnet_flags](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#a121a30fd546ccb887c2c49ceef65c2d6)
- [bt_mesh_cdb_subnet_key_import](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#aba737b508e0e40dfb5ad9da9d7b6fd11)
- [bt_mesh_cdb_subnet_key_export](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#ac361a17a704195e852faecda09881203)
- [bt_mesh_cdb_app_key_alloc](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#ab82dcdf26d66ea4ab0df34bc23421f39)
- [bt_mesh_cdb_app_key_del](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#a692c6980c9b0d2da18e8f47d67757f07)
- [bt_mesh_cdb_app_key_get](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#ab728a20fdb1535cc7059a39e8490a736)
- [bt_mesh_cdb_app_key_store](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#a4e9470adfa797be85b7f4df43b63d6d2)
- [bt_mesh_cdb_app_key_import](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#a9ad0651ccaa7ff1f86402ce8c05c9410)
- [bt_mesh_cdb_app_key_export](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#a87cfce7316efabe4c8b24be6c3b6d8b4)
- [atomic.h](../atomic_reference/P002_原子操作公共头文件参考.md)
- [mesh.h](../api_file_reference/P218_zephyr__bluetooth__mesh.h_文件参考.md)
- [bt_mesh_cdb_app_key::app_key](../bluetooth_mesh_model_reference/P024_bt_mesh_cdb_app_key_结构体.md#a2d685a7dd5e1f4678c34ea72be3fe6a2)
- [bt_mesh_cdb_app_key::app_idx](../bluetooth_mesh_model_reference/P024_bt_mesh_cdb_app_key_结构体.md#a2ef7f5d832b36736d3a1811a407b6fa6)
- [bt_mesh_cdb_app_key::keys](../bluetooth_mesh_model_reference/P024_bt_mesh_cdb_app_key_结构体.md#aa113eaa2a648cdabe21dc2c57b31bf65)
- [bt_mesh_cdb_app_key::net_idx](../bluetooth_mesh_model_reference/P024_bt_mesh_cdb_app_key_结构体.md#afa234a0d5f0fb61513a97afb91986976)
- [bt_mesh_cdb_node::num_elem](../bluetooth_mesh_model_reference/P025_bt_mesh_cdb_node_结构体.md#a2313e29b756344a493989f39ba1ec726)
- [bt_mesh_cdb_node::flags](../bluetooth_mesh_model_reference/P025_bt_mesh_cdb_node_结构体.md#a32f48db827713e53e02c0c1574476835)
- [bt_mesh_cdb_node::dev_key](../bluetooth_mesh_model_reference/P025_bt_mesh_cdb_node_结构体.md#a54e5130d7dabedf09e23419a40f6778b)
- [bt_mesh_cdb_node::uuid](../bluetooth_mesh_model_reference/P025_bt_mesh_cdb_node_结构体.md#a751671f52c4fdf3f42b6f71193976dd5)
- [bt_mesh_cdb_node::addr](../bluetooth_mesh_model_reference/P025_bt_mesh_cdb_node_结构体.md#a8c9941929a8ce6228817d76fe4e2375c)
- [bt_mesh_cdb_node::net_idx](../bluetooth_mesh_model_reference/P025_bt_mesh_cdb_node_结构体.md#aa936534676ef7e256670d356eff7ac17)
- [bt_mesh_cdb_subnet::kr_phase](../bluetooth_mesh_model_reference/P026_bt_mesh_cdb_subnet_结构体.md#a07fbd0e52571cd9a16e876243483e98a)
- [bt_mesh_cdb_subnet::net_idx](../bluetooth_mesh_model_reference/P026_bt_mesh_cdb_subnet_结构体.md#a1010965e2030e1bef181920fc5f76116)
- [bt_mesh_cdb_subnet::keys](../bluetooth_mesh_model_reference/P026_bt_mesh_cdb_subnet_结构体.md#a2f04c34ebbb8ae1e33f6679f94690c9a)
- [bt_mesh_cdb_subnet::net_key](../bluetooth_mesh_model_reference/P026_bt_mesh_cdb_subnet_结构体.md#a40d47a7705f4d3a9ba9349972d11072a)
- [bt_mesh_cdb::iv_index](../bluetooth_mesh_model_reference/P023_bt_mesh_cdb_结构体.md#a48b3cf852a42b580f911e193a9764517)
- [bt_mesh_cdb::app_keys](../bluetooth_mesh_model_reference/P023_bt_mesh_cdb_结构体.md#a59a130ffed26c362dc72d57d1ac7d7fd)
- [bt_mesh_cdb::nodes](../bluetooth_mesh_model_reference/P023_bt_mesh_cdb_结构体.md#a7af2ac65c8919c594b8283ff57b5b7fc)
- [bt_mesh_cdb::flags](../bluetooth_mesh_model_reference/P023_bt_mesh_cdb_结构体.md#aa2526502debab1add405fe6e2c475475)
- [bt_mesh_cdb::lowest_avail_addr](../bluetooth_mesh_model_reference/P023_bt_mesh_cdb_结构体.md#acb7f3ae85a5929b9cfc18531e1d98ab5)
- [bt_mesh_cdb::subnets](../bluetooth_mesh_model_reference/P023_bt_mesh_cdb_结构体.md#ae391c898d11257c484c4e8d1b38fd9dc)

---

[上一章](P002_audio.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P004_coap_client_tcp.h_源码浏览.md)
