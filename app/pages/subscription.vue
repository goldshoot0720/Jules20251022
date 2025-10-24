<script setup lang="ts">
const supabase = useSupabaseClient()
const isOpen = ref(false)
const isEditOpen = ref(false)
const selectedSubscription = ref(null)
const toast = useToast()

const columns = [
  { key: 'name', label: '名稱' },
  { key: 'nextdate', label: '下次付款日期' },
  { key: 'price', label: '價格' },
  { key: 'site', label: '網站' },
  { key: 'actions', label: '操作' }
]

const { data: subscriptions, refresh } = await useAsyncData('subscriptions', async () => {
  const { data } = await supabase.from('subscription').select('*')
  return data
})

const newSubscription = ref({
  name: '',
  site: '',
  account: '',
  price: 0,
  nextdate: '',
  note: ''
})

async function addSubscription() {
  const { data, error } = await supabase.from('subscription').insert([newSubscription.value])
  if (error) {
    toast.add({ title: 'Error', description: error.message, color: 'red' })
  } else {
    isOpen.value = false
    refresh()
    toast.add({ title: 'Success', description: 'Subscription added.', color: 'green' })
  }
}

function openEditModal(subscription) {
  selectedSubscription.value = { ...subscription }
  isEditOpen.value = true
}

async function updateSubscription() {
  const { data, error } = await supabase.from('subscription').update(selectedSubscription.value).eq('id', selectedSubscription.value.id)
  if (error) {
    toast.add({ title: 'Error', description: error.message, color: 'red' })
  } else {
    isEditOpen.value = false
    refresh()
    toast.add({ title: 'Success', description: 'Subscription updated.', color: 'green' })
  }
}

async function deleteSubscription(id) {
  const { data, error } = await supabase.from('subscription').delete().eq('id', id)
  if (error) {
    toast.add({ title: 'Error', description: error.message, color: 'red' })
  } else {
    refresh()
    toast.add({ title: 'Success', description: 'Subscription deleted.', color: 'green' })
  }
}
</script>

<template>
  <UCard>
    <template #header>
      <div class="flex justify-between">
        <h2 class="text-xl font-bold">Subscription Management</h2>
        <UButton @click="isOpen = true">Add Subscription</UButton>
      </div>
    </template>

    <UTable :rows="subscriptions" :columns="columns">
      <template #actions-data="{ row }">
        <UButton @click="openEditModal(row)" color="orange" variant="ghost" icon="i-heroicons-pencil-square" />
        <UPopover>
          <UButton color="red" variant="ghost" icon="i-heroicons-trash" />
          <template #panel>
            <div class="p-4">
              <p>Are you sure you want to delete this subscription?</p>
              <div class="flex justify-end mt-4">
                <UButton @click="deleteSubscription(row.id)" color="red">Delete</UButton>
              </div>
            </div>
          </template>
        </UPopover>
      </template>
    </UTable>

    <UModal v-model="isOpen">
      <UCard>
        <template #header>
          <h3 class="text-lg font-bold">Add New Subscription</h3>
        </template>
        <UForm :state="newSubscription" @submit.prevent="addSubscription">
          <UFormGroup label="名稱" name="name"><UInput v-model="newSubscription.name" /></UFormGroup>
          <UFormGroup label="下次付款日期" name="nextdate"><UInput v-model="newSubscription.nextdate" type="date" /></UFormGroup>
          <UFormGroup label="價格" name="price"><UInput v-model.number="newSubscription.price" type="number" /></UFormGroup>
          <UFormGroup label="網站" name="site"><UInput v-model="newSubscription.site" /></UFormGroup>
          <UButton type="submit">Save</UButton>
        </UForm>
      </UCard>
    </UModal>

    <UModal v-model="isEditOpen">
      <UCard>
        <template #header>
          <h3 class="text-lg font-bold">Edit Subscription</h3>
        </template>
        <UForm v-if="selectedSubscription" :state="selectedSubscription" @submit.prevent="updateSubscription">
          <UFormGroup label="名稱" name="name"><UInput v-model="selectedSubscription.name" /></UFormGroup>
          <UFormGroup label="下次付款日期" name="nextdate"><UInput v-model="selectedSubscription.nextdate" type="date" /></UFormGroup>
          <UFormGroup label="價格" name="price"><UInput v-model.number="selectedSubscription.price" type="number" /></UFormGroup>
          <UFormGroup label="網站" name="site"><UInput v-model="selectedSubscription.site" /></UFormGroup>
          <UButton type="submit">Update</UButton>
        </UForm>
      </UCard>
    </UModal>
  </UCard>
</template>
