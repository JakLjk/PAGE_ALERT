function deleteAlert(alert_id)
{
    fetch("/load/delete_alert",{
        method: "POST",
        body: JSON.stringify({alert_id: alert_id}),
    }).then((_res) => {
        window.location.href = "/pages";
    });    
    
}