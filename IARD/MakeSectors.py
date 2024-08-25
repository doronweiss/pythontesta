step=32.73
startWith = - step / 2.0 - 90.0
for idx in range(11):
    print('<Sector Grid.Row="0" Grid.Column="1" HorizontalAlignment="Center" Height="150" Width="150" Stroke="Blue" Fill="Transparent" StartAngle="{0:.2f}" SweepAngle="{1:.2f}"/>'.format(startWith, step))
    startWith += step