import styled from 'styled-components';

export default function Number(props) {
  return(
    <NumberContainer>
      <Value percentage={props.percentage}>{Math.round(props.value * 100) / 100}</Value>
      <Label unit>{props.unit}</Label>
      <Label>{props.label}</Label>
    </NumberContainer>
  );
}

const NumberContainer = styled.div`
  width: 240px;
  height: 190px;
  border-radius: 8px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  border: 1px solid #818181;
`;

const Value = styled.div`
  font-size: 72px;
  color: ${props => (["hsl(",((props.percentage)*120).toString(10),",75%,50%)"].join(""))};
`;

const Label = styled.div`
  color: ${props => (props.unit ? '#000' : '#818181')};
  margin-bottom: 10px;
`;