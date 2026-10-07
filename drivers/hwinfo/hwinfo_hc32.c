/*
 * Copyright The Zephyr HC32F4A0 Contributors
 * SPDX-License-Identifier: Apache-2.0
 */

#include <string.h>
#include <zephyr/drivers/hwinfo.h>
#include <zephyr/sys/byteorder.h>
#include <zephyr/sys/util.h>
#include <hc32_ll.h>

ssize_t z_impl_hwinfo_get_device_id(uint8_t *buffer, size_t length)
{
	stc_efm_unique_id_t uid;
	uint8_t id[12];

	EFM_GetUID(&uid);
	sys_put_be32(uid.u32UniqueID0, &id[0]);
	sys_put_be32(uid.u32UniqueID1, &id[4]);
	sys_put_be32(uid.u32UniqueID2, &id[8]);
	length = MIN(length, sizeof(id));
	memcpy(buffer, id, length);
	return length;
}
