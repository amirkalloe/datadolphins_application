const changeHash = (hash: string | undefined) => {
  const router = useRouter()
  if (typeof hash === 'string') {
    router.replace({
      hash: '#' + hash,
    })
  } else {
    router.replace({
      hash: '',
    })
  }
}

interface pageTitleInfo {
  title: string
  labelType: 'locale-index' | 'page-title'
}
const pageTitleInfo = ref<pageTitleInfo>({
  title: '',
  labelType: 'page-title',
})
const providePageTitle = (
  input: pageTitleInfo = { title: '', labelType: 'page-title' }
) => {
  pageTitleInfo.value = input
}

interface mappingUpc {
  name: string
  upc: string
}

const evtpNm = ref<mappingUpc>({
  name: '',
  upc: '',
})

const ggNm = ref<mappingUpc>({
  name: '',
  upc: '',
})

// (un)collapse
const activeItem = ref(
  [] as Array<{
    header: string
    active: boolean
    iconCollapse: string
    index: any
  }>
)
const hideUnhide = ref(true as boolean)
const hiddenText = ref('Overzicht uitklappen' as string)

const hideUnhideAll = (inputHidden: boolean) => {
  if (inputHidden) {
    activeItem.value.map((item) => (item.active = false))
    activeItem.value.map((item) => (item.iconCollapse = 'fa-chevron-up'))
    hiddenText.value = 'Overzicht inklappen'
    hideUnhide.value = false
  } else {
    activeItem.value.map((item) => (item.active = true))
    activeItem.value.map((item) => (item.iconCollapse = 'fa-chevron-down'))
    hiddenText.value = 'Overzicht uitklappen'
    hideUnhide.value = true
  }
}

const collapse = (header: string) => {
  hideUnhide.value = false
  hiddenText.value = 'Overzicht inklappen'
  const showSection = !activeItem.value
    .filter((item) => item.header === header)
    .map((item) => item.active)[0]
  activeItem.value
    .filter((item) => item.header === header)
    .map((item) => (item.active = showSection))
  const icon = showSection ? 'fa-chevron-down' : 'fa-chevron-up'
  activeItem.value
    .filter((item) => item.header === header)
    .map((item) => (item.iconCollapse = icon))
  return activeItem.value.filter((item) => item.header === header)
}

const hideHeader = (header: string) => {
  if (activeItem) {
    return activeItem.value
      .filter((item) => item.header === header)
      .map((item) => item.active)[0]
  } else return true
}

const getIconCollapse = (header: string) => {
  return activeItem.value
    .filter((item) => item.header === header)
    .map((item) => item.iconCollapse)[0]
}

const resetCollapse = () => {
  activeItem.value.map((item) => (item.active = true))
  activeItem.value.map((item) => (item.iconCollapse = 'fa-chevron-down'))
  hiddenText.value = 'Overzicht uitklappen'
  hideUnhide.value = true
}

export {
  changeHash,
  providePageTitle,
  pageTitleInfo,
  evtpNm,
  ggNm,
  hideHeader,
  collapse,
  hideUnhideAll,
  activeItem,
  hideUnhide,
  hiddenText,
  getIconCollapse,
  resetCollapse,
}
