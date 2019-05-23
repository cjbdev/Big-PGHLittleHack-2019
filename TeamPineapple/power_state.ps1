param (
    $vcenter,
    $folder,
    $user,
    $password,
    [switch] $start,
    [switch] $stop
)
connect-viserver $vcenter -user $user -password $password
$fldr = get-folder $folder
$vms = get-vm -location $fldr
if($start){
    $vms|Start-VM -RunAsync -Confirm:$false
}
elseif($stop){
    $vms|Stop-VM -RunAsync -Confirm:$false
}
